//FenceRepair
//長い板からN個の板を切り出します。
//切り出す板の長さはL1,L2,....,LNであり、元の板の長さはちょうどこれらの合計です。
//板を切断する際には、切断する板の長さ分のコストがかかります。
//すべての板を切り出す場合、最小でどれだけのコストがかかりますか。
//（コストの例）
//21の板を13と8に切断→21のコスト
//13の板を5と8に切断→13のコスト
//
//以前、貪欲法で解いたやつをプライオリティーキュー（ヒープ）で解く
//

#include <stdio.h>
#include <stdlib.h>

int sum(int*,int);
void swap(int*,int,int);
int downheap(int*,int,int);
void heap_sort(int*,int);

int main(void) 
{
    const int INF =100000000;  
    int N;
    int L[]={8,5,8,4,1,9};
    long answer =0;
    N = 6;

    heap_sort(L,N-1);// ヒープソートを行う

    //板が一枚になるまで適用（L[0]にしか数字が入っていない状態）
    while(L[1] != INF){
        int l1=0;
        int l2=0;
        
        l1 = L[0];
        L[0] = INF;

        l2 = L[1];
        L[1] = INF;
         
        heap_sort(L,N-1);// ヒープソートを行う
        
        answer += l1 + l2;

        //push処理
        for(int j=0;j<N;j++)
        {
            if(L[j]==INF)
            {
                L[j]= l1 + l2;
                heap_sort(L,N-1);
                break;
            }
        }
    }

    printf("%ld",answer);

    return 0;
}



//プライオリティーキュー（ヒープ）の作成（昇順）
//配列の成分の入れ替え
void swap(int* pArray,int m,int n)
{
    int tmp = pArray[m];
    pArray[m] = pArray[n];
    pArray[n] = tmp;
}
//  ヒープの要素を沈める処理。pArray[start]から、pArray[end]までを要素とする。
int downheap(int* pArray,int start,int end){
    int parent,child,r = 0;
    child = end;    //  子ノードのスタート位置
    //  末端の要素から、たどり、親要素よりも値が大きければ、入れ替える処理を繰り返す。
    do{
        //  親ノードの番号取得
        parent = start + (child - start) / 2;
        //  バイナリツリーの末端の最初が親よりも大きければ、入れ替える。
        if(pArray[child] < pArray[parent]){
            swap(pArray,child,parent);
            r = 1;
        }
        //  iをデクリメント
        child--;
    }while(parent > start);  //  子ノードが、startの位置を超えてしまったら、終了

    //1か0でrをreturn
    return r;
}


//  ヒープソート
void heap_sort(int* pArray,int size)
{
    int i = 0;
    while(downheap(pArray,i,size)){
        i++;
    }
}
