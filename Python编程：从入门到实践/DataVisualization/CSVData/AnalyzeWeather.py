# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AnalyzeWeather
   Description :
   Author :        Liangz
   Date：          2018/10/24
-------------------------------------------------
   Change Activity:
                   2018/10/24:
-------------------------------------------------
"""
__author__ = 'Liangz'


import csv


filename = 'sitka_weather_07-2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
