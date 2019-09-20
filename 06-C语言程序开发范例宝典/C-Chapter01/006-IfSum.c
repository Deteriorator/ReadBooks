/*
 * 实例 006 a^2 + b^2
 */

int IfSum(int a, int b)
{
    if (a * a + b * b > 100)
    {
        return a * a + b * b;
    }
    else
    {
        return a + b;
    }
}
