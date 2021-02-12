#Nの長さの文字列Sが与えられます。
#文字列Sを使って、長さNの新しい文字列Tを作ってください。
#なお、作成の際は、Tの値が辞書順比較でできるだけ小さくなるように作ること。
#また、文字列Tに対しては次のいずれかの操作が行える。
#
#・Sの先頭の１文字を削除し、Tの末尾に追加する。
#・Sの末尾の１文字を削除し、Tの末尾に追加する。
#
#アルゴリズムの答え
#「Sの先頭と末尾を比べ、小さい方を末尾に追加するを繰り返す」だと
# 先頭と末尾が同じケースを考慮しきれていない。
#よって、Sを反転させた「S'」を作成し「末尾と比べる」のではなく、S'と比べるようにする。
#・S[i]とS'[i]の比較で、Sが小さいのであれば、Sの先頭を１文字削除し、Tの末尾に追加する。
#・S'が小さいのであれば、Sの末尾を１文字削除し、Tの末尾に追加する。
#同じ文字になった場合は、S[i+1]、S'[i+1]を比較する・・・を繰り返して同じ文字が続かなくなるまで大小を評価する。

def main_method(N,S):

    #変数の宣言
    start_position = 0
    end_position = N-1
    output_T = []
    
    while start_position <= end_position:
        left_judge = False
        i = 0
        #左から見た場合(S)と右から見た場合(S')を比較
        #==のときはbreakしないので
        #同じ文字列が続いた場合であっても、先頭と末尾、どちらが小さくなるか判定できる
        while start_position + i <= end_position:
            if S[start_position + i] < S[end_position - i]:
                left_judge = True
                break

            elif S[start_position + i] > S[end_position-i]:
                left_judge = False
                break

            i = i + 1

        #Sのほうが小さいなら、S[i]を出力、そうでないならS'[i]を出力
        if left_judge:
            output_T.append(S[start_position])
            start_position = start_position + 1
        else:
            output_T.append(S[end_position])
            end_position = end_position - 1
    
            
    answer = ''.join(output_T)
    return answer

