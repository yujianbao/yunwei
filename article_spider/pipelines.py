# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import csv
import time, datetime
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
file_put_path = base_dir +'\\contents\\premiere_voice\\'
filepath = os.path.join(base_dir, 'contents')
aircraft = os.path.join(filepath, 'aircraft.csv')



class ArticleSpiderPipeline(object):
    """
    用来下载文章的
    """
    def process_item(self, item, spider):
        content_dict = dict(title="".join(item['title']), content="".join(item['content']), ref="".join(item['ref']),
                           key_words="".join(item['key_words']))
        content = json.dumps(content_dict, ensure_ascii=False)
        put_file = file_put_path + "".join(item['url_md5']) + '.json'
        if not os.path.exists(file_put_path):
            os.mkdir(file_put_path)
        with open(put_file, 'w', encoding='utf8') as f:
            f.write(content)
        return item

resall = []
aid = 100
aircraft_node = open(aircraft, 'a', newline='', encoding='utf-8')
country = {'美国': 20,
'中国': 21,
'英国': 22,
'法国': 23,
'德国': 24,
'苏/俄': 25,
'印度': 26,
'日本': 27,
'韩国': 28,
'以色列': 29,
'巴西': 30,
'意大利': 31,
'巴基斯坦': 32,
'波黑': 33,
'捷克': 34,
'南非': 35,
'西班牙': 36,
'伊朗': 37,
'乌克兰': 38,
'加拿大': 39,
'荷兰': 40,
'印度尼西亚': 41,
'波兰': 42,
'瑞士': 43,
'新西兰': 44,
'澳大利亚': 45,
'阿根廷': 46,
'新加坡': 47,
'奥地利': 48,
'智利': 49,
'比利时': 50,
'罗马尼亚': 51,
'瑞典': 52}

engine_count = {
	'单发': 71,
	'双发': 72,
	'三发': 73,
	'四发': 74,
	'六发': 75,
	'八发': 76
}

# 诞生期
dsq_ids = {
52:	'二战前',
53:	'二战期间',
54:	'二战后至冷战期间',
55:	'冷战后至今'
}
# 样式
style_ids = {
56:	'前掠翼',
57:	'后掠翼',
58:	'变后掠翼',
59:	'平直翼',
60:	'双翼',
61:	'鸭式',
62:	'无尾',
63:	'飞翼',
64:	'三角面',
65:	'单旋翼',
66:	'共轴双旋翼',
67:	'交叉双旋翼',
68:	'倾转旋翼',
69:	'纵列双旋翼',
70:	'并列双旋翼'
}


class ArmsSpiderPipeline(object):
    """
    用来处理武器信息的
    """

    def process_item(self, item, spider):
        # print(dir(item))
        # print(item)
        # assert item['content']
        res = {}
        if spider.name == 'weapon':
            res['content'] = item['content']
            res['src'] = item['src']
            res['ycg'] = item['ycg']
            res['datainfo'] = item['datainfo']
            # res['datalist'] = item['datalist']
            # res['xingneng'] = item['xingneng']
            res['othercontent'] = item['othercontent']
            res['suffix'] = item['suffix']
            res['child_url'] = item['child_url']


            res = json.dumps(res, ensure_ascii=False)
            with open('weapon1.json', 'a') as f:
                f.write(res + ',\n')

            return item
        elif spider.name == 'wuqi':
            content = item['content'] or ''
            datainfo = item['datainfo']
            src = item['src']
            ycg = item['ycg'][0]  # 原产国
            print(type(content), type(datainfo), type(src))
            d = {'名称：': 'name', '首飞时间：': 'firsttime', '服役时间：': 'fysj', '研发单位：': 'yfdw',
                 '气动布局：': 'qdbj', '发动机数量：': 'fdjsl', '飞行速度：': 'fxsd', '关注度：': 'gzd'}


            for data in datainfo:
                # print(data,type(data))
                if data in d.keys():
                    res[d[data]] = datainfo[datainfo.index(data) + 1]
            res['src'] = src

            res['ycg'] = ycg
            print(type(ycg), ycg)
            ycg_id = country[ycg] if ycg[0] in country else 21                    # 原产国
            fdjsl_id = engine_count[res['fdjsl']] if 'fdjsl' in res else '71'   # 发动机数量
            res['suffix'] = item['suffix']
            res['ycg_id'] = ycg_id
            res['fdjsl_id'] = fdjsl_id
            firsttime = res['firsttime']   # 处理诞生期
            reg = re.compile('\d+年')
            s='1985年4月'
            ss = reg.search(s).group()

            t1 = datetime.datetime.strptime(ss or '2018年', '%Y年')
            t2 = datetime.datetime.strptime('1939-09-01', "%Y-%m-%d")
            t3 = datetime.datetime.strptime('1945-09-02', "%Y-%m-%d")
            t4 = datetime.datetime.strptime('1991-12-25', "%Y-%m-%d")

            if t1 < t2:
                res['dsq_id'] = 52
                res['dsqsj'] = '二战前'
            elif t2 <= t1 <= t3:
                res['dsq_id'] = 53
                res['dsqsj'] = '二战期间'
            elif t3 < t1 <= t4:
                res['dsq_id'] = 54
                res['dsqsj'] = '二战后至冷战期间'
            else:
                res['dsq_id'] = 55
                res['dsqsj'] = '冷战后至今'


            res['content'] = content
            print(item['ycg'])
            print(res)

            w = csv.writer(aircraft_node)

            global aid
            aid = aid + 1
            if aid == 100:
                w.writerow(('name:ID', 'aircraft', ':LABEL'))  # 写入表头
            w.writerow((aid, res['name'], res['name']))  # 写入行
            # aircraft_node.close()
            res = json.dumps(res, ensure_ascii=False)
            with open('wuqi.json', 'a') as f:
                f.write(res + ',\n')

            return item


class VoiceSpiderPipeline(object):
    """
    用来爬取音频
    """
    def process_item(self, item, spider):
        content = item['content']
        put_file = file_put_path + item['url_md5'] + '.mp3'
        if not os.path.exists(file_put_path):
            os.mkdir(file_put_path)
        with open(put_file, 'wb') as f:
            f.write(content)
        return item


class VideoSpiderPipeline(object):
    """
    用来爬取音频
    """
    def process_item(self, item, spider):
        # print(item)
        # content = item['target_url']+"\n"
        # print("content", content)
        # with open("url_list.txt", 'a') as f:
        #     f.write(content)
            # print("insert_successfully!")
        return item