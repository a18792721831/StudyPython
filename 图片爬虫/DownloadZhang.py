import threading
import os
from GetWebObj import getWebObj
from Webp2Jpg import webp2Jpg


class downloadZhang(threading.Thread):
    def __init__(self, imgurl):
        threading.Thread.__init__(self)
        self.imgurl = imgurl

    def run(self):
        for key, value in self.imgurl.items():
            if not os.path.exists(key):
                os.mkdir(key)
            flag = 0
            for i in value:
                iph = key + '\\' + str(flag) + '.webp'
                webObj = getWebObj(i)
                iFile = open(iph, 'wb')
                iFile.write(webObj.content)
                iFile.close()
                webp2Jpg(iph)
                flag += 1
                print(key[key.rfind('\\') + 1 : len(key)] + '\t' + str(flag) + '\t页下载完成')