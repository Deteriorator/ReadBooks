/**<

【例2.1】求1×2×3×4×5。

 */

#include<stdio.h>

main(){
    int i, j, sum = 1;
    printf("请输入连乘的截止：");
    scanf("%d", &j);
    for(i = 1; i <= j; i++){
        sum = sum * i;
    }
    printf("结果：%d", sum);
}
