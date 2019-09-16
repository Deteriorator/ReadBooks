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
import pygal


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

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 Times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "结果频率"

hist.add('D6', frequencies)
hist.render_to_file('RollDiceVisual.svg')

print(frequencies)
