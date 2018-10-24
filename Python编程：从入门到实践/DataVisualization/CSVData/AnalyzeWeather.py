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
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取最高气温
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))

    # print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')

    # 设置图形的格式
    # plt.title(u'2014年7月每日最高气温', fontsize=24)
    # plt.xlabel('', fontsize=16)
    # plt.ylabel(u'温度（F）', fontsize=16)
    # plt.tick_params(axis='both', which='major', labelsize=16)

    # 中文不行
    plt.title(u'Daily Hhigh Temperatures-2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # plt.show()
    plt.savefig('wholeyear.png', bbox_inches='tight')
