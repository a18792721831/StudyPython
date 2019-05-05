from GetHtmlUtil import getHtml
from bs4 import BeautifulSoup
from demjson import decode
import re


def getMhInfo(url):
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    par = re.compile('var mh_info=\{.*?\}')
    script = re.search(par, str(soup))
    if script:
        par = re.compile(r'\{.*')
        script = re.search(par, script.group())
        return decode(str(script.group()))


url = "https://www.manhuatai.com/nitianxieshen/60.html"
print(getMhInfo(url))