//Expedition
//
//トラックで距離Lの道を移動する。トラックにはガソリンPが積まれているが、
//距離1走るごとにガソリンが減る。
//途中にはN個のガソリンスタンドがある。
//各ガソリンスタンドはスタート地点から距離Ai地点にあって、Biだけガソリンを補給することができる。
//トラックの燃料タンクの容量に制限はなく、ガソリンはいくらでも補給可能。
//途中でガソリンが0になってしまうと、トラックは停止してしまい、移動に失敗してしまう。
//移動を完了できる場合は最小のガソリン補給回数を答えなさい。
//移動を完了できない場合は-１を出力しなさい。
//
//
//アルゴリズムの答え
//・燃料が0になったときに、給油していたことにするかどうかを判断する
//・給油していたことにするガソリンスタンドは、給油量Biが多いものを選択した方が、給油回数が少なくて済む
//・ガソリンスタンドを通り過ぎたときに給油量をプライオリティーキューに格納する
//・燃料が0になったときに、プライオリティーキューが空であれば、移動は達成できない
//
//ヒープってプライオリティキューなので、配列でヒープソートかましてあげれば実現できる
//


#include <stdio.h>
#include <stdlib.h>
#define MAX_LENGTH  20000

int sum(int*,int);
void swap(int*,int,int);
int downheap(int*,int,int);
//void showData(int*,int);
void heap_sort(int*,int);

int main(void) 
{
    int L;
    int P;
    int goal;
    int N;
    int que[MAX_LENGTH] = {0};

    //入力
    L = 25;
    P = 10;
    N = 4;
    int A[] = {10,14,20,21};
    int B[] = {10,5,2,4};

    int ans = 0,pos = 0,tank = P;
    
    for (int i=0;i<N;i++)
    {
        //ガソリンスタンドまでの距離
        int d = A[i] - pos;

        //ガソリンが0未満になった時の処理
        while(tank - d< 0 )
        {
            //完走できないパターン
            if(sum(que,MAX_LENGTH)==0)
            {
                puts("-1");
                return 0;
            }
            
            tank += que[0];
            que[0] = 0;
            heap_sort(que,MAX_LENGTH);// ヒープソートを行う
            ans ++;
        }

        tank -= d;
        pos = A[i];
        
        //push処理
        for(int j=0;j<MAX_LENGTH;j++)
        {
            if(que[j]==0)
            {
                que[j]=B[i];
                heap_sort(que,MAX_LENGTH);
                break;
            }
        }
    }

    //答えをprint
    printf("%d\n",ans);

    return 0;
}

//sum関数
int sum(int* que,int n)
{
    int sum_num=0;
    for(int i = 0;i<n;i++)
    {
        sum_num = sum_num + que[i];
    }

    return sum_num;
}
 
//ヒープの作成（降順）
//  配列の成分の入れ替え
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
        if(pArray[child] > pArray[parent]){
            swap(pArray,child,parent);
            r = 1;
        }
        //  iをデクリメント
        child--;
    }while(parent > start);  //  子ノードが、startの位置を超えてしまったら、終了
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

