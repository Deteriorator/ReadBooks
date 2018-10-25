# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WorldPopulation
   Description :
   Author :        Liangz
   Date：          2018/10/25
-------------------------------------------------
   Change Activity:
                   2018/10/25:
-------------------------------------------------
"""
__author__ = 'Liangz'


import json


# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as file :
    pop_data = json.load(file)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ':' + population)

