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
from Ship import Ship
# from Alien import Alien
from Settings import Settings
import GameFunctions
from pygame.sprite import Group
from GameStatus import GameStatus
from Button import Button
from ScoreBoard import ScoreBoard

def run_game():
    # 初始化Pygame、设置和屏幕对象

    game_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(game_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    status = GameStatus(game_settings)

    scoreboard = ScoreBoard(game_settings, screen, status)

    # 设置背景色
    # bg_color = (230,230,230)

    # 创建一艘飞船
    ship = Ship(game_settings, screen)

    # 创建一个外星人
    # aliens = Alien(game_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    GameFunctions.create_fleet(game_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True :

        # 监控键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        GameFunctions.chech_events(game_settings, screen, status, scoreboard, play_button, ship, aliens, bullets)

        if status.game_active:
            ship.update()

            # 每次循环时都重回屏幕
            # screen.fill(game_settings.bg_color)
            # ship.blitme()
            #
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()

            # bullets.update()

            # 删除已消失的子弹
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)
            # print(len(bullets))

            GameFunctions.update_bullets(game_settings, screen, status, scoreboard, ship, aliens, bullets)
            GameFunctions.update_aliens(game_settings, screen, status, scoreboard, ship, aliens, bullets)
        GameFunctions.update_screen(game_settings, screen, status, scoreboard, ship, aliens, bullets, play_button)

run_game()
