# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json


base_dir = os.path.dirname(os.path.abspath(__file__))
file_put_path = base_dir +'\\contents\\premiere_voice\\'

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
        content = item['target_url']+"\n"
        print("content", content)
        with open("url_list.txt", 'a') as f:
            f.write(content)
            print("insert_successfully!")
        return item