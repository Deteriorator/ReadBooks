# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Americas
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
world_map.title = 'North, Central, and South America'

world_map.add('North America', ['ca', 'mx', 'us'])
world_map.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
world_map.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

world_map.render_to_file('Americas.svg')
