# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 16:46
# @Author  : Wang
# @FileName: test1.py
# @Software: PyCharm

from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>hello</p>', 'lxml')
print(soup.p.string)
