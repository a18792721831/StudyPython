import requests


def getWebObj(url):
    header = {
        'Accept': "*/*",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    if url is not None and url.strip() != '':
        return requests.request('GET', url = url.strip(), headers = header, timeout = 60)