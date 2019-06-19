# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 22:11
# @Author  : Wang
# @FileName: test_requests.py
# @Software: PyCharm

import requests

r = requests.get('http://www.baidu.com')
print('type of r: ', type(r))
print('status_code:', r.status_code)
print('type of text: ', type(r.text))
print('text of r: ', r.text)
print('cookies of r:', r.cookies)

print('---------------------------------------')
data = {
    'name': 'germey',
    'age': '22'
}
r = requests.get("http://httpbin.org/get", params=data)
print('text of r:', r.text)
print('json: ', r.json())
print('type of json: ', type(r.json()))