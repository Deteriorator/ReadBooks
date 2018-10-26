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
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

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

# 根据人口数量将所有的国家分成三组
world_population_1, world_population_2, world_population_3 = {}, {}, {}
for world_code, population in whole_population.items():
    if population < 10000000:
        world_population_1[world_code] = population
    elif population < 1000000000:
        world_population_2[world_code] = population
    else:
        world_population_3[world_code] = population

# 看看每组分别包含多少个国家
print(len(world_population_1), len(world_population_2), len(world_population_3))

world_map_style = RotateStyle('#336699', base_style=LightColorizedStyle)
# world_map_style = LightColorizedStyle
world_map = World(style=world_map_style)
world_map.title = 'World Population In 2010, By Country'
world_map.add('0 - 10M', world_population_1)
world_map.add('10M - 1BN', world_population_2)
world_map.add('>1BN', world_population_3)
world_map.render_to_file('threelevel_light_style.svg')
