# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from article_spider.items import ArmsSpiderItem
from article_spider.common.util import get_md5



class ChairmanSpider(scrapy.Spider):
    name = 'wuqi'
    allowed_domains = ['weapon.huanqiu.com']
    start_urls = ['http://weapon.huanqiu.com/weaponlist/aircraft']
    url = 'http://weapon.huanqiu.com/weaponlist/aircraft/list_0_0_0_0_'
    # 一共四页, ['index2.html', 'index3.html', 'index4.html']
    # index_list = ['index2.html', 'index3.html', 'index4.html']
    index_list = ['111', '110', '109', '108', '107', '106', '105', '104', '103', '102', '101', '100', '99',
                   '98', '97', '96', '95', '94', '93', '92', '91', '90', '89', '88', '87', '86', '85', '84',
                   '83', '82', '81', '80', '79', '78', '77', '76', '75', '74', '73', '72', '71', '70', '69',
                   '68', '67', '66', '65', '64', '63', '62', '61', '60', '59', '58', '57', '56', '55', '54',
                   '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39',
                   '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24',
                   '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9',
                   '8', '7', '6', '5', '4', '3', '2', '1']


    def start_requests(self):
        url = 'http://weapon.huanqiu.com/weaponlist/aircraft'
        yield Request(url=url, callback=self.parse_item)


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
        if len(self.index_list) != 0:
            next_url = self.url + self.index_list.pop()
            yield Request(url=next_url, callback=self.parse_item)

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
        # articleItemLoader.add_xpath('title', '//h1/text()')
        articleItemLoader.add_xpath('src', "//div[@class='maxPic']/img/@src")
        articleItemLoader.add_xpath('content', "//div[@class='intron']/div[@class='module']//text()")
        # articleItemLoader.add_xpath('name',"//div[@class='dataInfo']/ul[1]/li[1]/text() | //div[@class='dataInfo']/ul[1]/li[1]/span/text()")#.extract()[0].replace("\t", "")
        articleItemLoader.add_xpath('ycg', "//div[@class='maxPic']/span[@class='country']/b/a/text()")
        articleItemLoader.add_xpath('datainfo', "//div[@class='dataInfo']/ul[1]/li/span/text() | //div[@class='dataInfo']/ul[1]/li/text()")
        # articleItemLoader.add_xpath('datalist', "//ul[@class='dataList xh-highlight']/ul/li/span/text() | //ul[@class='dataList xh-highlight']/ul/li/b/text()")

        # articleItemLoader.add_xpath('key_words', "//meta[@name='keywords']/@content")
        # articleItemLoader.add_value('ref', response.url)
        # articleItemLoader.add_value('url_md5', url_md5)
        articleItemLoader.add_value('suffix', suffix)
        # key_words =  response.xpath("//meta[@name='keywords']/@content").extract()[0]
        articleInfo = articleItemLoader.load_item()

        # print("articleInfo", articleInfo)
        yield articleInfo
