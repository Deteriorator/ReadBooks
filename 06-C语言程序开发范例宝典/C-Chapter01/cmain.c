#include "stdafx.h"

int main()
{
    int a, b, c, result;
    printf("Please Input three numbers: ");
    //gets(i);
    scanf("%d %d %d", &a, &b, &c);
    result = IntegralMultiple(a, b, c);
    if (result == 1)
    {
        printf("yes");
    }
    else
    {
        printf("No");
    }
    getchar();
    getchar();
}
