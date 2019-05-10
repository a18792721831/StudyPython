def getNextZhangUrl(soup, mh_info):
    baseTag = soup.select("div[class='copyright'] > a:first-child")
    if len(baseTag):
        baseTag = baseTag.pop()
        nextTag = soup.select("a[class='mh_nextbook mh_btn']")
        for oneTag in nextTag:
            return 'https:' + baseTag['href'] + '/' + mh_info['mhid'] + '/' + oneTag['href']