import urllib.request
import urllib.parse
import socket
import urllib.error

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))  #输出网页源码
print('type of response: ', type(response))
print('status of response: ', response.status)
print('getheaders method: ', response.getheaders())
print('getheaders method containing parameters: ', response.getheader('Server'))

# 测试data参数
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print('read method: ', response.read())

# # 测试timeout参数, 单位为秒
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

# 测试error
print('--------test error---------')
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT!')