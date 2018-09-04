# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     EvenNumber
   Description :
   Author :        Liangz
   date：          2018/8/4
-------------------------------------------------
   Change Activity:
                   2018/8/4:
-------------------------------------------------
"""
__author__ = 'Liangz'


import optparse


def even(num):
    print('偶数')
    for i in range(1, num+1):
        if i % 2 == 0:
            print(i, end='\t')


def main():
    parse = optparse.OptionParser(u'使用方法 python EvenNumber.py -n <num>')
    parse.add_option('-n', dest='num', type='int', help=u'范围1-num')
    (options, args) = parse.parse_args()
    num = options.num
    even(num)


if __name__ == '__main__':
    main()
