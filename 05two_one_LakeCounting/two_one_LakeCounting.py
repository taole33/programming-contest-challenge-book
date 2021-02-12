#大きさが縦N　×　横Mにある枠の中で、
#水たまりの場所のデータが与えられるので、水たまりの数を数えなさい。
#水たまりはWで示されるが、周り８マスにWがある場合は、
#同一の水たまりとみなす。

def main_method(N,M,lake):
    yinput = int(N) #Nはy軸
    xinput = int(M) #Mはx軸
    lakelist = lake

    def dfs(y,x):
        #Wを.に置き換える
        lakelist[y][x] = "."        

        #周りにあるWも.に置き換える（同一の水たまりを全て.に変換する）
        for dx in range(-1,2):
            for dy in range(-1,2):
                checkx = x + dx
                checky = y + dy
                
                if 0 <= checkx < xinput and 0 <= checky < yinput and not lakelist[checky][checkx] == "." :
                    dfs(checky,checkx)
        return
    
    def searchw():
        output_count = 0
        for i in range(yinput):
            for j in range(xinput):
                if not lakelist[i][j] == ".":
                    dfs(i,j)
                    output_count = output_count + 1
        
        #dfsの実行回数が水たまりの数
        return output_count

    return(searchw())
