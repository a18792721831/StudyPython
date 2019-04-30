from GetTitle import getTitle


def getFiction(soup):
    fictionTag = soup.select('#content')
    if len(fictionTag):
        fictionTag = fictionTag.pop()
        result = '\n\n\n' + getTitle(soup) + '\n\n\n'
        result += fictionTag.text
        return result
