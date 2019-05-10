from GetHtmlUtil import getHtml
from bs4 import BeautifulSoup
import re


def getMhInfo(url):
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    par = re.compile('var mh_info=\{.*?\}')
    script = re.search(par, str(soup))
    if script:
        par = re.compile(r'\{.*')
        script = re.search(par, script.group())
        return script.group()


# url = "https://www.manhuatai.com/nitianxieshen/1.html"
# dic = eval(getMhInfo(url))
# print(type(dic))
# print(dic)