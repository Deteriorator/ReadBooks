#include "stdafx.h"

int main()
{
    int a, b;
    printf("Please Input two numbers: ");
    //gets(i);
    scanf("%d %d", &a, &b);
    printf("result is: %d", IfSum(a, b));
    getchar();
    getchar();
}
