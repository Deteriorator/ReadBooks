# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RandomWalk
   Description :
   Author :        Liangz
   Date：          2018/10/22
-------------------------------------------------
   Change Activity:
                   2018/10/22:
-------------------------------------------------
"""
__author__ = 'Liangz'


from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步

