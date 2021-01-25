#Lcmの竿の上にn匹のアリが毎秒1cmで歩く
#アリが出会うと、反対を向く
#竿の左端からの距離xはわかるが、どちらの方向を向いているかは不明。
#L,n.xの値が与えられているとき、
#すべてのアリが竿から落ちるまでにかかる最小の時間と最大の時間をそれぞれ求めよ。

#アリが出会うと反対を向く→アリの区別をなくすと、
#そのまますれ違ったとして扱っても同じ結果になる


def main_method(L,n,x):
    L = int(L)
    n = int(n)
    xlist = list(map(int,x.split()))

    #min
    min_output = 0
    for i in range(n):
        min_output = max(min_output,min(xlist[i],L-xlist[i]))

    #max
    max_output = 0
    for i in range(n):
        max_output = max(max_output,max(xlist[i],L-xlist[i]))
    
    return min_output,max_output




