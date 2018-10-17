# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GameStatus
   Description :
   Author :        Liangz
   Date：          2018/10/11
-------------------------------------------------
   Change Activity:
                   2018/10/11:
-------------------------------------------------
"""
__author__ = 'Liangz'



class GameStatus():

    """跟踪游戏的统计信息"""

    def __init__(self, game_settings):
        """初始化统计信息"""
        self.game_settings = game_settings
        self.reset_status()

        # 让游戏一开始处于非活动状态
        self.game_active = False

        # 在任何情况下都不重置最高得分
        self.high_score = 0

    def reset_status(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
