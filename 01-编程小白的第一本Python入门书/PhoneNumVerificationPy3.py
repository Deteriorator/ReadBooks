# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PhoneNumVerificationPy3
   Description :
   Author :        Liangz
   Date：          2018/9/6
-------------------------------------------------
   Change Activity:
                   2018/9/7:
-------------------------------------------------
"""
__author__ = 'Liangz'

import random


def send_num(phone_num):
    verification_code = random.randint(100000, 999999)
    print('Hi,用户',phone_num,'您好！\n 您的验证码是',verification_code)


def main():
    your_num = input("Enter Your Number : ")
    CN_MOBILE = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
    CN_UNION = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    CN_TELECOM = [133, 153, 180, 181, 189, 177, 1700]
    first_three = int(your_num[0:3])
    first_four = int(your_num[0:4])
    if len(your_num) != 11 :
        print('Invalid length, your number should be in 11 digits')
        main()
    else:
        # print(int(your_num[0:3]), type(int(your_num[0:3])), type(CN_MOBILE[1]))
        if first_three in CN_UNION or first_four in CN_UNION:
            print('Operator : China Union\nWe are sending verification code via text to your phone:',your_num)
            send_num(your_num)
        elif first_three in CN_TELECOM or first_four in CN_TELECOM:
            print('Operator : China Telecom\nWe are sending verification code via text to your phone:', your_num)
            send_num(your_num)
        elif first_three in CN_MOBILE or first_four in CN_MOBILE:
            print('Operator : China Mobile\nWe are sending verification code via text to your phone:',your_num)
            send_num(your_num)
        else:
            print('No such phone number!')

if __name__ == '__main__':
    main()