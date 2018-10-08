# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GameFunctions
   Description :
   Author :        Liangz
   Date：          2018/10/8
-------------------------------------------------
   Change Activity:
                   2018/10/8:
-------------------------------------------------
"""
__author__ = 'Liangz'

import sys
import pygame


def chech_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(game_setting, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(game_setting.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
