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
from pygame.sprite import Group
from Ship import Ship


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

        # 准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得放装换为一幅渲染的图像"""
        rounded_score = int(round(self.status.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.status.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.status.level), True, self.text_color, self.game_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示剩余的飞船数量"""
        self.ships = Group()
        for ship_number in range(self.status.ships_left):
            ship = Ship(self.game_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
