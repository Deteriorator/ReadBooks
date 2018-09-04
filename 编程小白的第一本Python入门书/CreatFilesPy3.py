# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CreatFiles
   Description :   快速创建文本
   Author :        Liangz
   date：          2018/8/4
-------------------------------------------------
   Change Activity:
                   2018/8/4:
-------------------------------------------------
"""
__author__ = 'Liangz'

import optparse


def create_file(num=1):
    for i in range(1, num+1):
        fp = open('{}.txt'.format(i), 'w')
        fp.close()


def main():
    parse = optparse.OptionParser(u'使用方法 python CreateFiles.py -n <num>')
    parse.add_option('-n', dest='num', type='int', help=u'创建文件的数量')
    (options, args) = parse.parse_args()
    num = options.num
    create_file(num)


if __name__ == '__main__':
    main()
