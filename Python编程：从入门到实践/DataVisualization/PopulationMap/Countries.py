# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Countries
   Description :
   Author :        Liangz
   Date：          2018/10/25
-------------------------------------------------
   Change Activity:
                   2018/10/25:
-------------------------------------------------
"""
__author__ = 'Liangz'


from pygal_maps_world.i18n import COUNTRIES


for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
