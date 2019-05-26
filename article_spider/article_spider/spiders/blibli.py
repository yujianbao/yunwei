import scrapy
from scrapy import Request
from article_spider.items import VoiceSpiderItem, VideoUrlItem
from article_spider.common.util import get_md5
from article_spider.common.util import parse_url
from scrapy.loader import ItemLoader
import json

"""
本爬虫用于爬取音频文档
"""

class VoiceSpider(scrapy.Spider):
    name = "bilibli"

    allowed_domains = ['api.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword=辩论赛&page=1']

    def start_requests(self):
        for i in range(1,21):
            url = "https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword=辩论赛&page={}".format(i)
            yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        result_json = json.loads(response.text)
        item = VideoUrlItem()
        datas = result_json['data']['result']
        # print(datas[0]["arcurl"])
        for res in datas:
            long_time = res['duration'].split(":")
            if int(long_time[0]) > 30:
                item['target_url'] = res['arcurl']
                yield item


