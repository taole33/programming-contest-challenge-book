#大きさが縦N　×　横M の迷路が与えられます。
#１ターンに上下左右に動くことができる。
#スタートからゴールまで移動するのに必要な最小のターン数を求めなさい。、

def main_method(N,M,maze):
    
    #変数の宣言
    INF = int(10000000);
    yinput = int(N) #Nはy軸
    xinput = int(M) #Mはx軸
    mazelist = maze
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = []

    #配列dをN×M分だけ作成する。（すべてのマス分の配列を用意する）
    #その配列ですべてのマスの移動回数を保持しておける。
    #まだ訪れてないところはINFでフラグを立てておく
    d = [[INF for i in range(xinput)] for j in range(yinput)]

    #Start地点を探す関数
    def start():
        for i in range(yinput):
            for j in range(xinput):
                if mazelist[i][j] == "S":
                    return i,j

    #Goal地点を探す関数
    def goal():
        for i in range(yinput):
            for j in range(xinput):
                if mazelist[i][j] == "G":
                    return i,j

    startyx = start()
    sy = startyx[0]
    sx = startyx[1]

    goalyx = goal()
    gy = goalyx[0]
    gx = goalyx[1]


    def address_maze():
        queue.append([sy,sx])
        d[sy][sx] = 0

        while not len(queue) == 0:
            popresult = queue.pop(0)
            resulty = popresult[0]
            resultx = popresult[1]
            if resulty == gy and resultx == gx:
                break

            for i in range(4):
                ny = resulty + dy[i]
                nx = resultx + dx[i]

                try:
                #if条件　x軸とy軸が枠から外れていないか。「#」に移動しようとしてないか。すでに通った場所（INF）に移動しようとしてないか。
                    if 0 <= nx <= xinput and 0 <= ny <= yinput and mazelist[ny][nx] !="#" and d[ny][nx] == INF:
                        queue.append([ny,nx])
                        #dに+1した距離を追加する
                        d[ny][nx] = d[resulty][resultx] + 1 
                except IndexError:
                    pass
                
        return d[gy][gx]

    return address_maze()
    





