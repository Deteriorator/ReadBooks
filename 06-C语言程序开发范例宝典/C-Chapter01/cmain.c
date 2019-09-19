#include "stdafx.h"

int main()
{
    int a, b, c;
    printf("Please Input three number: ");
    //gets(i);
    scanf("%d %d %d", &a, &b, &c);
    SortByAsc(a, b, c);
    getchar();
    getchar();
}
