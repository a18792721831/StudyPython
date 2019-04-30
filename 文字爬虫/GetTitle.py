def getTitle(soup):
    fictionTag = soup.select("div[class='bookname'] > h1")
    if len(fictionTag):
        fictionTag = fictionTag.pop()
        return fictionTag.text