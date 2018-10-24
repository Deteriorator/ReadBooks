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
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
