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
from CountryCode import get_country_code
from pygal_maps_world.maps import World

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as file:
    pop_data = json.load(file)

# 创建一个包含人口数量的字典
whole_population = {}

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # print(code + ':' + str(population))
            whole_population[code] = population
        # else:
        #     print('Error - ' + country_name)

world_map = World()
world_map.title = 'World Population In 2010, By Country'
world_map.add('2010', whole_population)

world_map.render_to_file('world_population.svg')
