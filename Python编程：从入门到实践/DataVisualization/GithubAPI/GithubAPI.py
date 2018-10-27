# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GithubAPI
   Description :
   Author :        Liangz
   Date：          2018/10/27
-------------------------------------------------
   Change Activity:
                   2018/10/27:
-------------------------------------------------
"""
__author__ = 'Liangz'


import requests


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:', r.status_code)

# 将API响应存储到一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys())
