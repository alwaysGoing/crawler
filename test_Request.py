import urllib.request

# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
responce = request.urlopen(req)
print(responce.read().decode('utf-8'))