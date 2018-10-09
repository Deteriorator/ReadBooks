# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Bullet
   Description :
   Author :        Liangz
   Date：          2018/10/9
-------------------------------------------------
   Change Activity:
                   2018/10/9:
-------------------------------------------------
"""
__author__ = 'Liangz'

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射的子弹"""
    def __init__(self, game_settings, screen, ship):
        """在飞船所在的位置创建子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

