"""
该爬虫用于爬取李克强讲话的内容
"""

import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from article_spider.items import PremiereSpiderItem
from article_spider.common.util import get_md5
import sys


class PremiereSpider(scrapy.Spider):
    name = 'premiere'
    allowed_domains = ['sousuo.gov.cn', 'www.gov.cn']
    start_urls = ['http://sousuo.gov.cn/column/30900/0.htm']

    def start_requests(self):
        url = "http://sousuo.gov.cn/column/30900/0.htm"
        yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        """
        获取当前页面问文章的列表
        :param response:
        :return:
        """
        for item in response.xpath("//div[@class='news_box']//ul/li"):
            base_url = item.xpath("./h4/a/@href").extract()
            if len(base_url) != 0:
                target_url = "".join(base_url)
                print("target_url", target_url)
                yield Request(url=target_url, callback=self.parse_article)
        next_page = response.xpath('//div[@class="newspage cl"]//ul/li/a/@href').extract()[-1]
        if next_page:
           yield Request(url=next_page, callback=self.parse_item)


    def parse_article(self, response):
        child_url = response.url
        print("child_url", child_url)
        url_md5 = get_md5(child_url)
        articleItemLoader = ItemLoader(item=PremiereSpiderItem(), response=response)
        articleItemLoader.add_xpath('title', "//h1/text() | //div[@class='pages-title']/text()")
        articleItemLoader.add_xpath('content', "//div[@class='pages_content']/p/text() | //div[@class='pages_content']//p/text()")
        articleItemLoader.add_xpath('key_words', "//meta[@name='keywords']/@content")
        articleItemLoader.add_value('ref', response.url)
        articleItemLoader.add_value('url_md5', url_md5)

        articleInfo = articleItemLoader.load_item()

        # print("articleInfo", articleInfo)
        yield articleInfo



