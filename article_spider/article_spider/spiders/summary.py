# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from article_spider.items import ArticleSpiderItem
from article_spider.common.util import get_md5


class SummarySpider(scrapy.Spider):
    name = 'summary'
    allowed_domains = ['gongwen.1kejian.com']
    start_urls = ['http://gongwen.1kejian.com/']

    def start_requests(self):
        url = 'http://gongwen.1kejian.com/list-19-1.html'
        yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        """
       爬取当前页面文章列表
       :param response:
       :return:
       """
        for item in response.xpath("//li[@class='atit']"):
            base_url = item.xpath("./a/@href").extract()[0]
            yield Request(url=base_url, callback=self.parse_article)
        next_page = response.xpath("//div[@id='pages']/a[@class='a1']/@href").extract()[1]
        if next_page:
            next_url = "http://gongwen.1kejian.com/"+next_page
            yield  Request(url=next_url, callback=self.parse_item)

    def parse_article(self, response):
        child_url = response.url
        url_md5 = get_md5(child_url)
        articleItemLoader = ItemLoader(item=ArticleSpiderItem(), response=response)
        articleItemLoader.add_xpath('title', '//h1/text()')
        articleItemLoader.add_xpath('content', "//div[@class='content']/p/text()")
        articleItemLoader.add_xpath('key_words', "//meta[@name='keywords']/@content")
        articleItemLoader.add_value('ref', response.url)
        articleItemLoader.add_value('url_md5', url_md5)
        articleInfo = articleItemLoader.load_item()

        # print("articleInfo", articleInfo)
        yield articleInfo