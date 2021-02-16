//ナップサック問題
//
//重さと価値がそれぞれwi,viであるようなn個の品物。
//重さの総和がWを超えないときの、価値の最大値は？
//

#include <stdio.h>

int max(int dp1, int dp2);

int main(void)
{
    int n,W;


    //入力
    n = 4;
    W = 5;
    int w[] = {2,1,3,2};
    int v[] = {3,2,4,2};

    int dp[n + 1][W + 1];

    for (int i = n-1;i>=0;i--){
        for(int j=0;j<=W;j++){
            if(j<w[i]){
                dp[i][j]=dp[i+1][j];
            }
            else{
                dp[i][j] = max(dp[i+1][j],dp[i+1][j-w[i]]+v[i]);
            }
        }
    }

    printf("%d\n",dp[0][W]);

}


int max(int dp1, int dp2) {
    if (dp1 > dp2)
        return dp1;
    else
        return dp2;
}