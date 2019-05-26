import scrapy
from scrapy import Request
from article_spider.items import VoiceSpiderItem, VideoUrlItem
from article_spider.common.util import get_md5
from article_spider.common.util import parse_url
from scrapy.loader import ItemLoader
import json

"""
本爬虫用于武器首页分类
"""

class VoiceSpider(scrapy.Spider):
    name = "weapon_index"

    allowed_domains = ['weapon.huanqiu.com']
    start_urls = ['http://weapon.huanqiu.com/weaponlist']

    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.parse_item)

    def parse_item(self, response):
        print(response.text)
        # result_json = json.loads(response.text)
        # print(result_json)
        # item = VideoUrlItem()
        # datas = result_json['data']['result']
        # print(datas[0]["arcurl"])
        # for res in datas:
        #     long_time = res['duration'].split(":")
        #     if int(long_time[0]) > 30:
        #         item['target_url'] = res['arcurl']
        #         yield item


