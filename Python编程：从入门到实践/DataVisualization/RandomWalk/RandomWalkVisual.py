# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RandomWalkVisual
   Description :
   Author :        Liangz
   Date：          2018/10/23
-------------------------------------------------
   Change Activity:
                   2018/10/23:
-------------------------------------------------
"""
__author__ = 'Liangz'


import matplotlib.pyplot as plt
from RandomWalk import RandomWalk


# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    random_walk = RandomWalk(50000)
    random_walk.fill_walk()
    point_numbers = list(range(random_walk.num_points))
    plt.scatter(random_walk.x_values, random_walk.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break
