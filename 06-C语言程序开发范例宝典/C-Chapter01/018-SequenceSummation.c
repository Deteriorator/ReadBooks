/*
 * 实例 018 序列求和
 */

double SequenceSummation(int n)
{
    int i = 1;
    double sum = 0;
    while (i <= n)
    {
        sum = sum + 1.0 / (double)i;
        i++;
    }
    return sum;
}

