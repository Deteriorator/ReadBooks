/*
 * 实例 004 以IP地址形式输出
 */

int BinToIP(int a[33])
{
    int ip[4];
    int i;
    for (i = 0; i < 8; i++)
    {
        if (a[i] == '1')
        {
            ip[0] += BinToDec(2, 7 - i);
        }
    }
    for (i = 8; i < 16; i++)
    {
        if (a[i] == '1')
        {
            ip[1] += BinToDec(2, 15 - i);
        }
    }
    for (i = 16; i < 24; i++)
    {
        if (a[i] == '1')
        {
            ip[2] += BinToDec(2, 23 - i);
        }
    }
    for (i = 24; i < 32; i++)
    {
        if (a[i] == '1')
        {
            ip[3] += BinToDec(2, 31 - i);
        }
    }
    return ip;
}

int BinToDec(int x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    return x * BinToDec(x, n - 1);
}