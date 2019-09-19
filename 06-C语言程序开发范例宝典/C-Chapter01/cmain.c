#include "stdafx.h"

int main()
{
    char i[33];
    int *ip = {0};
    printf("Please Input biniary number: ");
    //gets(i);
    scanf("%s", i);
    ip = BinToIP(i);
    printf("IP: %d.%d.%d.%d", ip[0], ip[1], ip[2], ip[3]);
    getchar();
    getchar();
}
