# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Alien-Invasion
   Description :
   Author :        Liangz
   Date：          2018/9/30
-------------------------------------------------
   Change Activity:
                   2018/9/30:
-------------------------------------------------
"""
__author__ = 'Liangz'

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏主循环
    while True :
        # 监控键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
