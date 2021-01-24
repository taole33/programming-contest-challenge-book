#n個の整数から三角形を作成することができるか判定するアルゴリズム
#三角形が作れないときは0をoutput
#三角形が作れるときは、一番長くなる周長をoutput
#三角形が作れるかどうかは、一番長い辺よりも、ほかの二辺の和の方が長い場合

def triangle(n,intlist):
    n = int(n)
    intlist = list(map(int,intlist.split()))

    answer = 0

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                three_edge_length = intlist[i] + intlist[j] + intlist[k]
                max_length = max(intlist[i],intlist[j],intlist[k])
                two_edge_length = three_edge_length - max_length

                if max_length < two_edge_length and answer < three_edge_length:
                    answer = three_edge_length

    return answer