//int BaseNToDec(char* x, int base)
//{
//    long result;
//    int i, t, t3;
//    //gets(x);
//    t3 = strlen(*x);
//    result = 0;
//    for (i = 0; i < t3; i++)
//    {
//        if (x[i] - '0' >= base && x[i] < 'A' || x[i] - 'A' + 10 >= base)  /*判断输入的数据和进制数是否相符*/
//        {
//            printf("输入有误!!");                         /*输出错误*/
//            exit(0);                                     /*退出程序*/
//        }
//        if (x[i] >= '0' && x[i] <= '9')                           /*判断是否为数字*/
//            t = x[i] - '0';                                       /*求出该数字赋给t*/
//        else if (base >= 11 && (x[i] >= 'A' && x[i] <= 'A' + base - 10))     /*判断是否为字母*/
//            t = x[i] - 'A' + 10;                                 /*求出字母所代表的十进制数*/
//        result = result * base + t;                              /*求出最终转换成的十进制数*/
//    }
//    printf("十进制形式是%ld\n", result);                          /*将最终结果输出*/
//}


