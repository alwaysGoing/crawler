# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 8:57
# @Author  : Wang
# @FileName: test3.py
# @Software: PyCharm

# Post 请求
import requests
data = {
    'name': 'germey',
    'age': '22'
}

r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
