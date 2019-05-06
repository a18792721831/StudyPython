from demjson import decode
import re


def getMhInfo(soup):
    par = re.compile('var mh_info=\{.*?\}')
    script = re.search(par, str(soup))
    if script:
        par = re.compile(r'\{.*')
        script = re.search(par, script.group())
        return decode(str(script.group()))