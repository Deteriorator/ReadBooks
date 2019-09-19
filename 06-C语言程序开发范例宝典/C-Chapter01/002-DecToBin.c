/*
 * 实例 002 十进制转换为二进制
 */
long DecToBin(int x)
{
    int remainder, temp;    //remainder 是余数
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

int DecToBinII(int x)
{
    int a[16] = { 0 };
    int i, m;
    for (m = 0; m < 15; m++)
    {
        i = x % 2;
        x = x / 2;
        a[m] = i;
    }
    for (m = 15; m >= 0; m--)
    {
        printf("%d", a[m]);
        if (m % 4 == 0)
        {
            printf(" ");
        }
    }
}
