"""
用于启动爬虫的函数入口
"""

from scrapy.cmdline import execute
import os
import sys


base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)



if __name__ == '__main__':
    # execute(['scrapy', 'crawl', 'chairman'])
    # execute(['scrapy', 'crawl', 'summary'])
    # execute(['scrapy', 'crawl', 'premiere'])
    # execute(['scrapy', 'crawl', 'bilibli'])
    # execute(['scrapy', 'crawl', 'wuqi'])
    execute(['scrapy', 'crawl', 'weapon'])