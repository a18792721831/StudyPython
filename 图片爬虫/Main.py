from GetHtmlUtil import getHtml
from bs4 import BeautifulSoup

# url = 'https://www.manhuatai.com/nitianxieshen/yg.html'
#
# html = getHtml(url)
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
#
# url = 'https://static.321mh.com/js/comic.read.min.js?20190428170732'
#
# html = getHtml(url)
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# url = 'https://www.manhuatai.com/nitianxieshen/yg.html'
# html = getHtml(url)
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
#
# str1 = "P'4H'G;':2':8'G7'C6'C;'G;':4'CC'G9'C7';G'4H'G;'C4':6'G7';3':C'4H"



# https://mhpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F4.jpg-mht.middle.webp
# https://mhpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F3.jpg-mht.middle.webp
# https://mhpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F3.jpg-mht.middle.webp
# https://mhpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F4.jpg-mht.middle.webp
# https://mhpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F5.jpg-mht.middle.webp

url = "https://mhpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F4.jpg-mht.middle.webp"
# https://m/hpic.manhualang.com/comic/N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F%E9%A2%84%E5%91%8A%2F4.jpg-mht.middle.webp
import os
import requests
from GetWebObj import getWebObj
file = open('E:\\img\\1.webp', 'wb')
file.write(getWebObj(url).content)
file.close()
