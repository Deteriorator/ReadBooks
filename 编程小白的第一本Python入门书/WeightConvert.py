# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WeightConvert
   Description :   重量单位换算
   Author :        Liangz
   date：          2018/8/3
-------------------------------------------------
   Change Activity:
                   2018/8/3:
-------------------------------------------------
"""
__author__ = 'Liangz'

import optparse


def convert(num):
    weight = float(num/1000)
    print( u'The Weight is : %s KG' %weight)


def main():
    parse = optparse.OptionParser(u'使用方法 python WeightConvert.py -w <num>')
    parse.add_option('-w', dest='weight', type='float', help=u'多少克')
    (options, args) = parse.parse_args()
    weight = options.weight
    convert(weight)


if __name__ == '__main__':
    main()
