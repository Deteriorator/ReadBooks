# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BetGamePy3
   Description :   赌点儿钱吧！
   Author :        Liangz
   date：          2018/9/6
-------------------------------------------------
   Change Activity:
                   2018/9/6:
-------------------------------------------------
"""
__author__ = 'Liangz'

import random


def throw_the_dice(num=3, pointlist=None):
    print('=========== 投掷骰子 ==========')
    if pointlist == None:
        pointlist = []

    for i in range(1, num+1):
        point = random.randrange(1, 7)
        pointlist.append(point)

    return pointlist


def result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'b'
    elif isSmall:
        return 's'


def main(money):
    print('=========== 开始游戏 ===========')
    choice = ['b', 's']
    print('==== b is big | s is small ==== ')
    your_choice = input('请输入你的选择：')
    bet = input('你想赌多少？-')
    if your_choice in choice:
        pointlist = throw_the_dice()
        total = sum(pointlist)
        win = your_choice == result(total)
        if win :
            print('The points are', pointlist, 'sum', total,'You win !')
            money = money + int(bet)
            print('You gained '+bet+'￥, you have '+ str(money)+ ' ￥ now')
        else:
            print('The points are', pointlist, 'sum', total,'You lost !')
            money = money - int(bet)
            print('You lost ' + bet + '￥, you have ' + str(money) + ' ￥ now')
        if money <= 0 :
            print('Game Over')
        else:
            main(money)


    else:
        print('Invalid Words')
        main(money)

if __name__ == '__main__':
    money = 1000
    print('Attention！！！ \n 初始金额为1000￥ \n 金额为0时游戏结束\n 默认赔率为1倍，押对得到相应的金额，押错了输掉相应金额\n\n')
    main(money)