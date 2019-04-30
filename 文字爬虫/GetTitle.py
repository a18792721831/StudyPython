def getTitle(soup):
    fictionTag = soup.select("div[class='bookname'] > h1")
    if len(fictionTag):
        fictionTag = fictionTag.pop()
        return fictionTag.text


# from GetHtmlUtil import getHtml
# from bs4 import BeautifulSoup
#
# html = getHtml('http://www.xbiquge.la/13/13959/5939025.html')
# soup = BeautifulSoup(html)
# print(getTitle(soup))