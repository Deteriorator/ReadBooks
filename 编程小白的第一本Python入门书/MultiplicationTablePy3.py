# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MultiplicationTablePy3
   Description :   使用Python实现9x9乘法表
   Author :        Liangz
   date：          2018/8/4
-------------------------------------------------
   Change Activity:
                   2018/9/4:
-------------------------------------------------
"""
__author__ = 'Liangz'

# for i in range(1, 10):
#     for j in range(1,10):
#         print("{}X{}={}".format(i,j,i*j))

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("{}X{}={}".format(i, j, i*j), end='\t')
    print()





