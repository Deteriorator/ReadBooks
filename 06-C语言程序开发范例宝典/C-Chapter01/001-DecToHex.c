#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

/*
 *ʵ�� 001 ʮ����ת��Ϊʮ������
 */
int DecToBin(int x);

void main()
{
    int i;
    printf("Please Input decimalism number: ");
    scanf("%d", &i);
    /*
     * ֱ��ʹ�ÿ����ַ���
     * %o �˽���
     * %x %X ʮ������
     */
    printf("the hex number is 0x%x\n", i);
    printf("the oct number is %o\n", i);
    printf("the bin number is %d\n", DecToBin(i));
    getchar();
    getchar();
}

// ʮ����ת������
long DecToBin(int x)
{
    int remainder, temp;    //remainder ������
    long result = 0, k = 1;
    temp = x;
    while (temp)
    {
        remainder = temp % 2;
        result = remainder * k + result;
        k = k * 10;
        temp = temp / 2;
    }
    return result;
}


/*
���� char *itoa(int value, char *string, int radix)
   ����ֵ����char
   ����value ��ת��������
   ����string ת����洢��string��
   ����radix ת����������
������ stdlib.h

ʾ����
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