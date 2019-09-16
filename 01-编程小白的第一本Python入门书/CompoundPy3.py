# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CompoundPy3
   Description :   复利计算函数
   Author :        Liangz
   date：          2018/8/4
-------------------------------------------------
   Change Activity:
                   2018/9/4:
-------------------------------------------------
"""
__author__ = 'Liangz'


import optparse


def invest(amount, rate=0.05, time=1):
    print('本金:{}'.format('$'+str(amount)))
    for i in range(1, time+1):
        amount = amount *(rate + 1)
        print('year {}: {}'.format(i, '$'+str(amount)))


def main():
    parse = optparse.OptionParser(u'使用方法 python CompoundPy3.py -a <amount> -r <rate> -t <time>')
    parse.add_option('-a', dest='amount', type='float', help=u'本金')
    parse.add_option('-r', dest='rate', type='float', help=u'利率，可以是小数')
    parse.add_option('-t', dest='time', type='int', help=u'时间/年，为整数')
    (options, args) = parse.parse_args()
    amount = options.amount
    rate = options.rate
    time = options.time
    invest(amount, rate, time)


if __name__ == '__main__':
    main()
