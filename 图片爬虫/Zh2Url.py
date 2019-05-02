import urllib.request


def zh2Url(sourceStr):
    return urllib.request.quote(sourceStr)


source = '逆天邪神'
print(source)
print(zh2Url(source))