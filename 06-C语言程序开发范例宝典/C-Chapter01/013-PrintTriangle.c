/*
 * 实例 013 用#打印三角形
 */

void PrintTriangle(int line)
{
    int i, j, k;
    for (i = 1; i < line; i++)
    {
        for (j = 1; j < line - i; j++)
        {
            printf(" ");
        }
        for (k = 1; k <= 2 * i - 1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}