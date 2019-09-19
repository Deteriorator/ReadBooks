/*
 * 实例 005 3个数有小到大排序
 */

void SortByAsc(int a, int b, int c)
{
    int temp;
    if (a > b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    if (a > c)
    {
        temp = a;
        a = c;
        c = temp;
    }
    if (b > c)
    {
        temp = b;
        b = c;
        c = temp;
    }
    printf("The order of the number is: %d %d %d", a, b, c);
}
