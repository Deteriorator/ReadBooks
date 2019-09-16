# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     NorthAmericaPopulation
   Description :
   Author :        Liangz
   Date：          2018/10/26
-------------------------------------------------
   Change Activity:
                   2018/10/26:
-------------------------------------------------
"""
__author__ = 'Liangz'


from pygal_maps_world.maps import World


world_map = World()

world_map.title = 'Populations Of Countries In North America'
world_map.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

world_map.render_to_file('NA_population.svg')

