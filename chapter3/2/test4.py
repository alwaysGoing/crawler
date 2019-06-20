# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 8:59
# @Author  : Wang
# @FileName: test4.py
# @Software: PyCharm

# 测试响应
import requests

r = requests.get('http://www.baidu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
