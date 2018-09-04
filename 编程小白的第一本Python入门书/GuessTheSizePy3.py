# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GuessTheSize
   Description :   简单的投掷骰子的游戏
   Author :        Liangz
   date：          2018/8/7
-------------------------------------------------
   Change Activity:
                   2018/8/7:
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


def main():
    print('=========== 开始游戏 ===========')
    choice = ['b', 's']
    print('==== b is big | s is small ==== ')
    your_choice = input('请输入你的选择：')
    if your_choice in choice:
        pointlist = throw_the_dice()
        total = sum(pointlist)
        win = your_choice == result(total)
        if win :
            print('The points are', pointlist, 'sum', total,'You win !')
        else:
            print('The points are', pointlist, 'sum', total,'You lost !')

    else:
        print('Invalid Words')
        main()

if __name__ == '__main__':
    main()
