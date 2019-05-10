def getNextZhangUrl(soup):
    baseTag = soup.select("div[class='header_logo'] > a")
    if len(baseTag):
        baseTag = baseTag.pop()
        nextTag = soup.select("div[class='bottem2'] > a")
        for oneTag in nextTag:
            if oneTag.text == '下一章' and oneTag['href'].endswith('.html'):
                return baseTag['href'] + oneTag['href']


from GetHtmlUtil import getHtml
from bs4 import BeautifulSoup


url = 'https://www.manhuatai.com/nitianxieshen/yg.html'
html = getHtml(url)
soup = BeautifulSoup(html)
print(getNextZhangUrl(soup))