//長い板からN個の板を切り出します。
//切り出す板の長さはL1,L2,....,LNであり、元の板の長さはちょうどこれらの合計です。
//板を切断する際には、切断する板の長さ分のコストがかかります。
//すべての板を切り出す場合、最小でどれだけのコストがかかりますか。
//（コストの例）
//21の板を13と8に切断→21のコスト
//13の板を5と8に切断→13のコスト

//このアルゴリズムの答え
//半分ずつに切っていくのが最短のコストになり、
//（長い板を残しておくと切断の度にコストがかかるため、できるだけ短くしたほうが良い→半分にしたほうがよい）
//その場合は、二分木で表すことができる。
//コストの合計は二分木の「葉×接点の深さ」の合計で求められる。
//今回のアルゴリズムはO(N*N)になってしまうが、O(NlogN)で解く方法もある。


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(int mii1,int mii2);

int main(void)
{
    int N;
    int L[]={8,5,8};
    long long answer =0;
    N = 3;

    while(N>1){
        int mii1 = 0, mii2 = 1;
        if(L[mii1] > L[mii2])
        {
            swap(mii1,mii2);
        }

        for (int i=2;i<N;i++)
        {
            if(L[i]<L[mii1]){
                mii2=mii1;
                mii1=i;
            }
            else if(L[i]<L[mii2])
            {
                mii2=i;
            }
        }

        int t = L[mii1] + L[mii2];
        answer += t ;

        if(mii1 == N-1)
        {
            swap(mii1,mii2);
        }
        L[mii1] = t;
        L[mii2] = L[N-1];
        N--;
    }

    printf("%lld\n",answer);

}


void swap(int mii1,int mii2)
{
	int temp;
	temp = mii1;
	mii1 = mii2;
	mii2 = temp;
	
    return;

}