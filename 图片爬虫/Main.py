from GetWebObj import getWebObj
from GetImagePath import getImagePath
from GetMhInfo import getMhInfo
from bs4 import BeautifulSoup
from GetHtmlUtil import getHtml
from GetNextZhangUrl import getNextZhangUrl
from Webp2Jpg import webp2Jpg
import queue
import os

zhangUrl = queue.Queue()
print('Please input first url:')
zhangUrl.put(input())
print('Please input save path:')
savePath = input()
imgUrl = queue.Queue()
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
    imgPath = getImagePath(mh_info)
    zhangPath = savePath + '\\' + mh_info['pagename']
    if mh_info[''].__eq__(str('你愿意为梦想付费吗')):
        print(url)
    imgUrl.put({zhangPath : imgPath})
    while not imgUrl.empty():
        one = imgUrl.get().items()
        for key in one :
            if not os.path.exists(key[0]) :
                os.mkdir(key[0])
            flag = 0
            for i in key[1]:
                iph = key[0] + '\\' + str(flag) + '.webp'
                webObj = getWebObj(i)
                iFile = open(iph, 'wb')
                iFile.write(webObj.content)
                iFile.close()
                webp2Jpg(iph)
                flag += 1