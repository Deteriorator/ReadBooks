#include "stdafx.h"

int main()
{
    int year, result;
    printf("Please Input year: ");
    //gets(i);
    scanf("%d", &year);
    result = JudgeYear(year);
    if (result == 1)
    {
        printf("%d is a leap year", year);
    }
    else
    {
        printf("%d is not a leap year", year);
    }
    getchar();
    getchar();
}
