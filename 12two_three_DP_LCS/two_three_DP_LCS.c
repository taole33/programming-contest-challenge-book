//最長共通部分列問題
//
//２つの文字列s1s2....snとt1t2....tmが与えられる。
//これら２つの共通部分文字列の長さの最大値を求めなさい。
//
//漸化式
//dp[i+1][j+1] = {max(dp[i][j]+1,dp[i][j+1],dp[i+1][j])(si+1=ti+1)
//               {max(dp[i][j+1],dp[i+1][j])(それ以外)



#include <stdio.h>

int max(int dp1, int dp2);

int main(void){
    int n,m;
    char *s;
    char *t;


    //入力
    n = 4;
    m = 4;
    s = "abcd";
    t = "becd";

    //dpテーブル
    int dp[n + 1][m + 1];

    //dpテーブルを作成する
    for (int i = 0;i<n;i++){
        for(int j=0;j<m;j++){
            if (s[i]==t[j]){
                dp[i+1][j+1] = dp[i][j]+1;
            } else {
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j]);
            }
        }
    }

    //dp[n][m]に答えが格納されてる
    printf("%d\n",dp[n][m]);

}


int max(int dp1, int dp2) {
    if (dp1 > dp2)
        return dp1;
    else
        return dp2;
}
