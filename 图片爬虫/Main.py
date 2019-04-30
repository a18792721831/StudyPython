from GetHtmlUtil import getHtml
from bs4 import BeautifulSoup

url = 'https://www.manhuatai.com/nitianxieshen/yg.html'

html = getHtml(url)
soup = BeautifulSoup(html, 'html.parser')
print(soup)


def getPicUrl():
    var i = lines[chapter_id].use_line
    , o = "." + (mh_info.image_suffix || "jpg").toLowerCase()
    , t = parseInt(mh_info.startimg) + e - 1 + o
    , n = "https://" + i + "/comic/" + mh_info.imgpath + t;
return __cr.switchWebp(n, mh_info.comic_size)