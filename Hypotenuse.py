# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Hypotenuse
   Description :   已知直角三角形两直角边，求斜边
   Author :        Liangz
   date：          2018/8/3
-------------------------------------------------
   Change Activity:
                   2018/8/3:
-------------------------------------------------
"""
__author__ = 'Liangz'

import optparse
import math


def hypotenuse(a, b):
    result = math.sqrt((a*a + b*b))
    print("The Right Triangle Third Side's Tength is %s" % result)


def main():
    parse = optparse.OptionParser(u'使用方法 python WeightConvert.py -a <num1> -b <num2>')
    parse.add_option('-a', dest='Leg1', type='float', help=u'直角边长度')
    parse.add_option('-b', dest='Leg2', type='float', help=u'直角边长度')
    (options, args) = parse.parse_args()
    leg1 = options.Leg1
    leg2 = options.Leg2
    args.append(leg2)
    hypotenuse(leg1, leg2)


if __name__ == '__main__':
    main()
