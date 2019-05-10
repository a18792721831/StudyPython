def getNextZhangUrl(soup, mh_info):
    baseTag = soup.select("div[class='copyright'] > a:first-child")
    if len(baseTag):
        baseTag = baseTag.pop()
        nextTag = soup.select("a[class='mh_nextbook mh_btn']")
        for oneTag in nextTag:
            return 'https:' + baseTag['href'] + '/' + mh_info['mhid'] + '/' + oneTag['href']

#
# from GetHtmlUtil import getHtml
# from bs4 import BeautifulSoup
# from GetMhInfo import getMhInfo
#
#
# url = 'https://www.manhuatai.com/nitianxieshen/60.html'
# html = getHtml(url)
# soup = BeautifulSoup(html, 'html.parser')
# print(getNextZhangUrl(soup, getMhInfo(url)))