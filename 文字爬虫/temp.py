import requests

url = "http://www.xbiquge.la/13/13959/5939025.html"

payload = ""
headers = {
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Host': "www.xbiquge.la",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive"
}

response = requests.request("GET", url, data=payload, headers=headers)
response.encoding = 'ISO-8809-1'
print(response.text)