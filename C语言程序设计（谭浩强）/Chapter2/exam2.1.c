/**<

����2.1����1��2��3��4��5��

 */

#include<stdio.h>

main(){
    int i, j, sum = 1;
    printf("���������˵Ľ�ֹ��");
    scanf("%d", &j);
    for(i = 1; i <= j; i++){
        sum = sum * i;
    }
    printf("�����%d", sum);
}
