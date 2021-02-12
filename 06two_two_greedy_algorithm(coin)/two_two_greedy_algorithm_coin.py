#１、５、１０，５０、１００，５００円玉の枚数が与えられます。
#Ａ円を支払うのに最小の枚数を計算しなさい。


def main_method(coins,A):

    #変数の宣言
    value_coins = [1,5,10,50,100,500]
    answer = 0
    payment = A
   
    for i in reversed(range(len(value_coins))):
        #払えるコイン数＝ayment//value_coins[i]
        #使えるコイン数＝coins[i]
        #どちらか小さい方を使う
        use_coins = min(payment//value_coins[i] , coins[i])
        payment = payment - use_coins * value_coins[i]
        answer = answer + use_coins

    return answer
