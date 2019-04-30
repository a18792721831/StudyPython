from GetTitle import getTitle


def getFiction(soup):
    fictionTag = soup.select('#content')
    if len(fictionTag):
        fictionTag = fictionTag.pop()
        result = '\n\n\n' + getTitle(soup) + '\n\n\n'
        result += fictionTag.text
        return result

# from GetHtmlUtil import getHtml
#
# html = getHtml('http://www.xbiquge.la/13/13959/5939025.html')
# print(getFiction(html))
