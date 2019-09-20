/*
 * 实例 007 整倍数
 */

int IntegralMultiple(int a, int x, int y)
{
    if ((a%x == 0) && (a%y == 0))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
