#整数a1,a2,...anが与えられます。
#その中からいくつか選び、その和をちょうどkにすることができるか判定しなさい。

def main_method(n,a,k):
    n = int(n)
    alist = list(map(int,a.split()))
    k = int(k)

    def dfs(i,sum):
        # i == nが終了条件。戻り値はBoolean
        if i == n :
            return sum == k
     
        #以下２つのif文でaを足し算に入れるかどうかを条件分けする
        #ここの条件が再帰的になっていることによって、
        #足すか？足さないか？の全てのパターンが網羅されている 
        if dfs(i+1,sum):
            return True

        if dfs(i+1,sum + alist[i-1]):
            return True
        
        return False

    return dfs(0,0)






