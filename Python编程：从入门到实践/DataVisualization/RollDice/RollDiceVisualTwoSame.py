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
dice_1 = RollDice()
dice_2 = RollDice()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 Times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "结果"
hist.y_title = "结果频率"

hist.add('D6 + D6', frequencies)
hist.render_to_file('RollDiceVisualTwoSame.svg')

print(frequencies)
