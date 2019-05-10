import requests
import time


def getWebObj(url):
    header = {
        'Accept': "*/*",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    if url is not None and url.strip() != '':
        flag = 0
        while flag < 20:
            try:
                return requests.request('GET', url = url.strip(), headers = header, timeout = 60)
            except:
                if flag < 20 :
                    time.sleep(2)
                    continue
                else:
                    print(url)
                    return None