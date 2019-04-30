from bs4 import BeautifulSoup


def getNextUrl(soup):
    baseTag = soup.select("div[class='header_logo'] > a")
    if len(baseTag):
        baseTag = baseTag.pop()
        nextTag = soup.select("div[class='bottem2'] > a")
        for oneTag in nextTag:
            if oneTag.text == '下一章' and oneTag['href'].endswith('.html'):
                return baseTag['href'] + oneTag['href']


# from GetHtmlUtil import getHtml
# html = getHtml('http://www.xbiquge.la/13/13959/5939025.html')
# print(getNextUrl(html))

# print(getNextUrl(html=html))