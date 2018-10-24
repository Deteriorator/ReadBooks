# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RollDiceVisual
   Description :
   Author :        Liangz
   Date：          2018/10/24
-------------------------------------------------
   Change Activity:
                   2018/10/24:
-------------------------------------------------
"""
__author__ = 'Liangz'


from RollDice import RollDice


# 创建一个D6
dice = RollDice()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    result = dice.roll()
    results.append(result)

print(results)
