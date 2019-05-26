import scrapy
from scrapy import Request
from article_spider.items import VoiceSpiderItem
from article_spider.common.util import get_md5
from article_spider.common.util import parse_url
from scrapy.loader import ItemLoader

"""
本爬虫用于爬取音频文档
"""

class VoiceSpider(scrapy.Spider):
    name = "voice"

    allowed_domains = ['sousuo.gov.cn', 'www.gov.cn']
    start_urls = ['http://sousuo.gov.cn/column/30639/0.htm']

    def start_requests(self):
        url = "http://sousuo.gov.cn/column/30639/0.htm"
        yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        for item in response.xpath("//ul[@class='listTxt']/li/h4"):
            base_url = item.xpath("./a/@href").extract()[0]
            yield Request(url=base_url, callback=self.parse_voice)
        next_page =  response.xpath("//div[@class='newspage cl']//li/a/@href").extract()[-1]
        if next_page:
            yield Request(url=next_page, callback=self.parse_item)

    def parse_voice(self, response):
        src_voice = response.xpath("//div[@id='audio_list']//li/a/@data-src").extract()[0]
        content = response.xpath("//div[@class='pages_content']/p/text()").extract()
        voice_url = parse_url(src_voice)
        text_contents = {"datas": content}
        yield Request(url=voice_url, callback=self.save_voice, meta=text_contents)

    def save_voice(self, response):
        mp3_content = response.body
        url_md5 = get_md5(response.url)
        item = VoiceSpiderItem()
        item['content'] = mp3_content
        item['url_md5'] = url_md5

        yield item


