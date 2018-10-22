# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ScatterDiagram
   Description :   散点图
   Author :        Liangz
   Date：          2018/10/22
-------------------------------------------------
   Change Activity:
                   2018/10/22:
-------------------------------------------------
"""
__author__ = 'Liangz'

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=5)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
