# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 22:22
# @Author  : Wang
# @FileName: test1.py
# @Software: PyCharm

# p125, 以知乎发现为例

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
print(r.text)