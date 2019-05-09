from GetImagePath import getImagePath
from GetMhInfo import getMhInfo
from bs4 import BeautifulSoup
from GetHtmlUtil import getHtml
from GetNextZhangUrl import getNextZhangUrl
from DownloadZhang import downloadZhang
import queue

zhangUrl = queue.Queue()
print('Please input first url:')
zhangUrl.put(input())
print('Please input save path:')
savePath = input()
print('Please input reference:')
refStr = input()
while not zhangUrl.empty():
    url = zhangUrl.get()
    try:
        html = getHtml(url)
    except:
        zhangUrl.put(url)
        continue
    soup = BeautifulSoup(html, 'html.parser')
    mh_info = getMhInfo(soup)
    zhangUrl.put(getNextZhangUrl(soup, mh_info))
    imgPath = getImagePath(mh_info, refStr)
    try:
        zhangPath = savePath + '\\' + mh_info['pagename']
    except:
        print(mh_info)
        continue
    if mh_info['pagename'].__eq__(str('你愿意为梦想付费吗')):
        continue
    downloadThrea = downloadZhang({zhangPath : imgPath})
    downloadThrea.start()