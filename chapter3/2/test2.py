# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 8:54
# @Author  : Wang
# @FileName: test2.py
# @Software: PyCharm

# p125, 抓取二进制文件
import requests
r = requests.get('https://github.com/favicon.ico')
print(r.text)
print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
