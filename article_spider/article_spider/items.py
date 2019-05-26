# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import Join
from scrapy.loader.processors import TakeFirst


def convert_content(data_list:list):
    contents_str = ""
    try:
        for contents in data_list:
            contents_str += format_content(contents)
    except Exception as e:
        print(sys.exc_info())
        contents_str =""
    return contents_str

def format_content(data:str):
    target_contents = data.replace('\n\t', "").strip()
    return "".join(target_contents)




class ArticleSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    default_output_processor=TakeFirst()
    title = scrapy.Field()
    content = scrapy.Field(
        input_processor=MapCompose(convert_content),
        output_processor=Join("\n")
    )
    key_words = scrapy.Field()
    ref = scrapy.Field()
    url_md5 = scrapy.Field()

class PremiereSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    default_output_processor=TakeFirst()
    title = scrapy.Field()
    content = scrapy.Field(
        input_processor=MapCompose(convert_content),
        output_processor=Join("\n")
    )
    key_words = scrapy.Field()
    ref = scrapy.Field()
    url_md5 = scrapy.Field()

class VoiceSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    default_output_processor=TakeFirst()
    content = scrapy.Field()
    url_md5 = scrapy.Field()
    text_content = scrapy.Field()


class VideoUrlItem(scrapy.Item):
    target_url = scrapy.Field()

