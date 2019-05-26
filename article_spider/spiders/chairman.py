# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from article_spider.items import ArticleSpiderItem
from article_spider.common.util import get_md5



class ChairmanSpider(scrapy.Spider):
    name = 'chairman'
    allowed_domains = ['cpc.people.com.cn']
    start_urls = ['http://cpc.people.com.cn/']
    url = 'http://cpc.people.com.cn/GB/64192/105996/352007/'
    # 一共四页, ['index2.html', 'index3.html', 'index4.html']
    index_list = ['index2.html', 'index3.html', 'index4.html']

    def start_requests(self):
        url = 'http://cpc.people.com.cn/GB/64192/105996/352007/'
        yield Request(url=url, callback=self.parse_item)


    def parse_item(self, response):
        """
        爬取当前页面文章列表
        :param response:
        :return:
        """
        for item in response.xpath("//div[@class='p2j_con02 clearfix w1000']/div[@class='fl']/ul/li"):
            target_url = item.xpath('./a/@href').extract()
            target_url = 'http://cpc.people.com.cn'+ "".join(target_url)
            yield Request(url=target_url, callback=self.parse_article)
        if len(self.index_list) != 0:
            next_url = self.url + self.index_list.pop()
            yield Request(url=next_url, callback=self.parse_item)

    def parse_article(self, response):
        child_url = response.url
        url_md5 = get_md5(child_url)
        articleItemLoader = ItemLoader(item=ArticleSpiderItem(), response=response)
        articleItemLoader.add_xpath('title', '//h1/text()')
        articleItemLoader.add_xpath('content', "//div[@class='show_text']//p/text()")
        articleItemLoader.add_xpath('key_words', "//meta[@name='keywords']/@content")
        articleItemLoader.add_value('ref', response.url)
        articleItemLoader.add_value('url_md5', url_md5)
        # key_words =  response.xpath("//meta[@name='keywords']/@content").extract()[0]
        articleInfo = articleItemLoader.load_item()

        # print("articleInfo", articleInfo)
        yield articleInfo
