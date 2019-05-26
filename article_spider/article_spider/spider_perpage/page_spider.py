import requests
from lxml import etree

def spider(url:str):
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }
    request = requests.get(url=url, headers=my_headers)
    content = request.text

    res = parse_content(content)

def parse_content(text: str):
    sel = etree.HTML(text)
    content = sel.xpath("//div[@class='content']/text()")
    final_content = ""
    for item in content:
        final_content += item.replace("\t", "")

    print("final", final_content)

    return content

def run_spider(url:str):
    spider(url=url)


if __name__ == '__main__':
    target_url = "http://gongwen.1kejian.com/show-26-93077-1.html"
    spider(url=target_url)
