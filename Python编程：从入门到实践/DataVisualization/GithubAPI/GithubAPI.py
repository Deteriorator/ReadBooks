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
import pygal
from pygal.style import LightColorizedStyle, LightenStyle


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:', r.status_code)

# 将API响应存储到一个变量中
response_dict = r.json()
print('Total Repositories:', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories Returned:', len(repo_dicts))

names, stars = [], []
# 研究第一个仓库
# repo_dict = repo_dicts[0]
print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    # print(key)
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    # print("\nSelected information about first repository:")
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description:', repo_dict['description'])

# 处理结果
# print(response_dict.keys())

# 可视化
my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Project On Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('Python-repos.svg')
