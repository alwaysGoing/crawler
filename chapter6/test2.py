# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 15:39
# @Author  : Wang
# @FileName: test2.py
# @Software: PyCharm

import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re
import time

def get_page(offset):
    headers = {
        'cookie': 'uuid="w:63cf916ebee445629e31f829f03b6040"; _ga=GA1.2.1920411327.1508761813; tt_webid=6727820039531677191; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6727820039531677191; passport_auth_status=ecb691fb6ce6cd9a66a87f14ebb961f9; sso_auth_status=ad22c3848c4e225706f4b045e48eb78f; sso_uid_tt=1a25821209b6f4aa9491c74f8a32a09a; toutiao_sso_user=40df7e5afc1e90be3593c5d793545948; login_flag=5389617dab2bf0ea575c3be1b622d1c2; sessionid=d9b1f4ae5ff03530e77cfb000979ee8e; uid_tt=245b0fe0e7d1d80751f2f128e2440577; sid_tt=d9b1f4ae5ff03530e77cfb000979ee8e; sid_guard="d9b1f4ae5ff03530e77cfb000979ee8e|1566442771|15552000|Tue\\054 18-Feb-2020 02:59:31 GMT"; s_v_web_id=b371ab0c530a10e7f2e1ba48f1407925; csrftoken=aed5c252ad0fd09cfdc82af3c1e52dcb; __tasessionId=eme7sfxx11566463948022',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    }
    time_stamp = int(time.time())
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': time_stamp
    }
    base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'
    url = base_url + urlencode(params)
    print(url)
    try:
        resp = requests.get(url, headers=headers)
        # print(resp)
        if 200 == resp.status_code:
            return resp.json()
    except requests.ConnectionError:
        return None

def get_image(json):
    # print(json)
    if json.get('data'):
        data = json.get('data')
        # print(data)
        for item in data:
            # if item.get('title') is None:
            #     continue
                # cell_type字段不存在的这类文章不爬取，它没有title，和image_list字段，会出错
            if item.get('cell_type') is not None:
                continue
            title = re.sub('[\t]', '', item.get('title'))
            # title = item.get('title').replace(' |?:', ' ')
            images = item.get('image_list')
            for image in images:
                origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                yield{
                    'image': origin_image,
                    'title': title
                }

def save_image(item):
    img_path = 'F:\\photo\\toutiao\\' + item.get('title')
    # print(img_path)
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(file_name=md5(resp.content).hexdigest(), file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s ' % file_path)
            else:
                print('Already Downloaded ', file_path)
    except Exception as e:
        print(e)

def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        save_image(item)

GROUP_START = 0
GROUP_END = 9

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    # for i in groups:
    #     main(groups)
