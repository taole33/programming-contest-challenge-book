//N個の点が直線状にあります。
//N個のうちのいくつかを選び、それらの点に印をつけます。
//N個のすべての点について、距離がR以内の場所に印をつけられた点がなければなりません、。
//条件を満たすうち、印がついた点が最小のパターンでは、何個の点に印をつける必要があるでしょうか。

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compareInt(const void* a, const void* b)
{
    int aNum = *(int*)a;
    int bNum = *(int*)b;

    return aNum - bNum;
}

int main(void)
{
    int N,R;
    const int MAX_N = 1000;
    int X[MAX_N];
    int length;
    int j;
    printf("点の数Nを入力してください\n");
    scanf("%d", &N);
    printf("距離Rを入力してください\n");
    scanf("%d", &R);

    for(j=0;j<N;j++)
    {
        printf("点%dの距離を入力してください\n",j);
        scanf("%d", &X[j]);
    }

    
    qsort(X, N, sizeof(int), compareInt);
    
    int i = 0, ans = 0;
    int s = 0, p = 0;
    
    while(i<N){
        s =X[i++];
        while(i<N && X[i] <= s + R) i++;
        
        p = X[i-1];
        while(i<N && X[i]<=p + R) i++;
        ans++;
    }

    printf("答えは %d です\n",ans);

}