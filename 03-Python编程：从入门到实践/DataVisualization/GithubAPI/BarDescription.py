# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BarDescription
   Description :
   Author :        Liangz
   Date：          2018/10/29
-------------------------------------------------
   Change Activity:
                   2018/10/29:
-------------------------------------------------
"""
__author__ = 'Liangz'


import pygal
from pygal.style import LightColorizedStyle, LightenStyle

my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'Django', 'Flask']

plot_dict = [
    {'value': 16101, 'label': 'Dedcription of httpie'},
    {'value': 15028, 'label': 'Description of Django'},
    {'value': 14798, 'label': 'Description of Flask'}
]

chart.add('', plot_dict)
chart.render_to_file('bar_description.svg')
