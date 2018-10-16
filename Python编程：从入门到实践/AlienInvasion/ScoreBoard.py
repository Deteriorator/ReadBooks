# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ScoreBoard.py
   Description :
   Author :        Liangz
   Date：          2018/10/15
-------------------------------------------------
   Change Activity:
                   2018/10/15:
-------------------------------------------------
"""
__author__ = 'Liangz'

import pygame.font

class ScoreBoard():
    """显示得分信息的类"""

    def __init__(self, game_settings, screen, status):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.status = status

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()

    def prep_score(self):
        """将得放装换为一幅渲染的图像"""
        score_str = str(self.status.score)

