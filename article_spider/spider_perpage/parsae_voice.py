import requests


def spider(url:str):
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }
    request = requests.get(url=url, headers=my_headers)
    content = request.content
    with open("01.mp3", 'wb') as f:
        f.write(content)


def run_spider(url:str):
    spider(url=url)

if __name__ == '__main__':
    target_url = 'http://www.gov.cn/xhtml/gov_audio/201904080942.Mp3'
    spider(url=target_url)
