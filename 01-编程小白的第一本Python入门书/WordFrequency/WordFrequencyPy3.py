# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WordFrequencyPy3
   Description :
   Author :        Liangz
   Date：          2018/9/11
-------------------------------------------------
   Change Activity:
                   2018/9/11:
-------------------------------------------------
"""
__author__ = 'Liangz'


import string

path = './Walden.txt'
with open(path, 'r', encoding='utf-8') as file:
    words = [fixed_word.strip(string.punctuation).lower() for fixed_word in file.read().split()]
    words_index = set(words)    # 转换为集合，去除重复单词
    count_word = {word_index:words.count(word_index) for word_index in words_index}
    # for word in words:
    #     print('{} : {} times'.format(word, words.count(word)))

for word in sorted(count_word, key=lambda x:count_word[x], reverse=True):
    print('{} : {} times'.format(word, count_word[word]))

print('\nTotal length : {}'.format(len(words)))
# print(words)
# print(words_index)
# print(len(words))
# print(string.punctuation)