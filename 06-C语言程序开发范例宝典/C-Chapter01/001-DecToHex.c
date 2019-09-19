/*
 *实例 001 十进制转换为十六进制
 */

//void main()
//{
//    int i;
//    printf("Please Input decimalism number: ");
//    scanf("%d", &i);
//    /*
//     * 直接使用控制字符串
//     * %o 八进制
//     * %x %X 十六进制
//     */
//    printf("the hex number is 0x%x\n", i);
//    printf("the oct number is %o\n", i);
//    printf("the bin number is %d\n", DecToBin(i));
//    getchar();
//    getchar();
//}

void DecToHex(int x)
{
    printf("the hex number is 0x%x\n", x);
}

// 十进制转二进制
//long DecToBin(int x)
//{
//    int remainder, temp;    //remainder 是余数
//    long result = 0, k = 1;
//    temp = x;
//    while (temp)
//    {
//        remainder = temp % 2;
//        result = remainder * k + result;
//        k = k * 10;
//        temp = temp / 2;
//    }
//    return result;
//}


/*
函数 char *itoa(int value, char *string, int radix)
   返回值类型char
   参数value 待转换的数字
   参数string 转换后存储到string中
   参数radix 转换到几进制
定义在 stdlib.h

示例：
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main()
{
    int userinput;
    printf("Please enter a integer.\n");
    scanf("%d",&userinput);

    char octal[MAX],hex[MAX];
    itoa(userinput,octal,8);
    itoa(userinput,hex,16);

    printf("Octal and Hex of the integer %d that you entered is %s and %s.\n",userinput,octal,hex);

    return 0;
}

*/