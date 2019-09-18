#include "stdafx.h"

int main()
{
    int i;
    printf("Please Input decimalism number: ");
    scanf("%d", &i);
    DecToHex(i);
    printf("the bin number is %d\n", DecToBin(i));
    BaseNToDec((char*)i, 8);
    DecToBinII(i);
    getchar();
    getchar();
}
