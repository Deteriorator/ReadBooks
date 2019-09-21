/*
 * 实例 008 判断闰年
 */

int JudgeYear(int year)
{
    /*if (year % 400 == 0)
    {
        return 1;
    }
    else if (year % 100 == 0)
    {
        return 0;
    }
    else if (year % 4 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }*/
    if ((year % 4 == 0) && (year % 100 != 0 || year % 400 == 0))
    {
        return 1;
    }
    else
    {
        return 0;
    }

}
