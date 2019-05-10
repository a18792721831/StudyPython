from GetHtmlUtil import getHtml
from GetNextUrlUtil import getNextUrl
from queue import Queue
from bs4 import BeautifulSoup
from GetFictionContext import getFiction
from SaveFiction import saveFiction
from MergeMiniFile import mergeFile
import os


print('Please input first page url:')
firstUrl = input()
print('Please input save path:')
savePath = input()
print('Please input saving file name:')
saveName = input()
cacheQueue = Queue()
nextUrl = firstUrl
urlQueue = Queue()
urlQueue.put(firstUrl)
tempDir = savePath + '\\temp'
print('Will be create temp dir')
if not os.path.exists(tempDir) :
    os.mkdir(tempDir)
print('start :url=' + firstUrl + '\tfilePath:' + savePath + '\\' + saveName)
flag = 0
try:
    while not urlQueue.empty():
        cacheName = urlQueue.get()
        print('start' + str(flag) + ':' + cacheName if cacheName else '')
        html = getHtml(cacheName)
        if html.strip() != '' :
            soup = BeautifulSoup(html, 'html.parser')
            urlQueue.put(getNextUrl(soup))
            cachePath = tempDir + '\\' + str(hash(cacheName)) + '.txt'
            saveFiction(getFiction(soup), cachePath)
            cacheQueue.put(cachePath)
        print('end:' + cacheName)
        flag += 1
except BaseException as err:
    print('getMini Error')
    print(err)
saveRealPath = savePath + '\\' + saveName
print('start Merge')
try:
    while not cacheQueue.empty():
        mergeFile(saveRealPath, cacheQueue.get())
except:
    print('Merge Error')
print('end Merge')
os.rmdir(savePath + '\\temp\\')
print('delete temp dir')
print('project is down')