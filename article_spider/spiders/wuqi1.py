# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from article_spider.items import ArmsSpiderItem
from article_spider.common.util import get_md5



class ChairmanSpider(scrapy.Spider):
    name = 'weapon'
    allowed_domains = ['weapon.huanqiu.com']
    start_urls = ['http://weapon.huanqiu.com/weaponlist/aircraft',
                  'http://weapon.huanqiu.com/weaponlist/warship',
                  'http://weapon.huanqiu.com/weaponlist/guns',
                  'http://weapon.huanqiu.com/weaponlist/tank',
                  'http://weapon.huanqiu.com/weaponlist/artillery',
                  'http://weapon.huanqiu.com/weaponlist/missile',
                  'http://weapon.huanqiu.com/weaponlist/spaceship',
                  'http://weapon.huanqiu.com/weaponlist/explosive',
                  ]
    # url = 'http://weapon.huanqiu.com/weaponlist/aircraft/list_0_0_0_0_'
    # 一共四页, ['index2.html', 'index3.html', 'index4.html']


    def start_requests(self):
        url = 'http://weapon.huanqiu.com/weaponlist/aircraft'
        yield Request(url=url, callback=self.parse_item)
        # urls = self.start_urls
        # for url in urls:
        #     yield Request(url=url, callback=self.parse_item)


    def parse_item(self, response):
        """
        爬取当前页面文章列表
        :param response:
        :return:
        """
        for item in response.xpath("//div[@class='picList']/ul/li"):
            # print(item.extarct())
            base_url = item.xpath("./span[@class='pic']/a/@href").extract()
            target_url = 'http://weapon.huanqiu.com'+ "".join(base_url)
            # target_url = item.xpath("./span[class='pic']/a/@href").extract()
            # print(2,type(target_url),target_url)
            # target_url = 'http://weapon.huanqiu.com'+ "".join(target_url)
            yield Request(url=target_url, callback=self.parse_article)

        for url in response.xpath("//div['pages']/a/@href").extract():
            # print('-----------------------------')
            # print(url)
            if url.find('/list_') >= 0:
                url = 'http://weapon.huanqiu.com%s' % url
                yield Request(url=url, callback=self.parse_item)


    def parse_article(self, response):
        child_url = response.url
        print(response.url)
        suffix = child_url.split('/')[-1]
        url_md5 = get_md5(child_url)
        # item = ArmsSpiderItem()
        # name = response.xpath("//div[@class='dataInfo']/ul[1]/li[1]/text()").extract()[0].replace("\t", "")
        # print("name",name)
        # item['name'] = name
        # content = response.xpath("//div[@class='intron']/div[@class='module']/p/text()").extract()[0]
        # item['content'] = content.replace("\t"，)

        articleItemLoader = ItemLoader(item=ArmsSpiderItem(), response=response)
        articleItemLoader.add_xpath('src', "//div[@class='maxPic']/img/@src")
        articleItemLoader.add_xpath('content', "//div[@class='intron']/div[@class='module']//text()")
        articleItemLoader.add_xpath('ycg', "//div[@class='maxPic']/span[@class='country']/b/a/text()")
        articleItemLoader.add_xpath('datainfo', "//div[@class='dataInfo']/ul[1]/li/span/text() | //div[@class='dataInfo']/ul[1]/li/text()")
        # articleItemLoader.add_xpath('datalist', "//div[@class='dataInfo']/u2[@class='dataList']/li//text() ")
        # articleItemLoader.add_xpath('xingneng', "//div[@class='dataInfo']/u3[@class='dataList']/li//text()")

        articleItemLoader.add_xpath('othercontent', "//div[@class='info']/div[@class='module']//text()")

        articleItemLoader.add_value('suffix', suffix)
        articleItemLoader.add_value('child_url', child_url)
        articleInfo = articleItemLoader.load_item()

        # print("articleInfo", articleInfo)
        yield articleInfo
