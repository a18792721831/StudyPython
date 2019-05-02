import re


def getZhangPageCount(strInfo):
    par = re.compile(r'totalimg:.*?,')
    result = re.search(par, strInfo)
    if result:
        strCount = result.group()
        numPar = re.compile(r'\d+')
        count = re.search(numPar, strCount)
        if count:
            return count.group()