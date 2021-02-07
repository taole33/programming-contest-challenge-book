#n個の仕事があります。各仕事はSi時間に始まり、Ti時間に終わります。
#それぞれの仕事について、参加、不参加を選ぶ場合、
#最多の仕事数を計算しなさい。
#参加する仕事の時間帯が重なってはいけませんし、開始の瞬間、終了の瞬間が重なるのも許されません。

#このアルゴリズムの答え
#終了時間が最も早いものを選ぶことを繰り返す

def main_method(n,start_time,end_time):

    #変数の宣言
    answer = 0
    newest_end_time = 0
    sort_pair = []

    #終了時間の早い順にソートするため、終了時間と開始時間のペアを作り、ソートする。
    for i in range(n):
        sort_pair.append((end_time[i],start_time[i]))
    sort_pair.sort()

    for i in range(n):
        if newest_end_time < sort_pair[i][1]:
            answer = answer + 1
            newest_end_time = sort_pair[i][0]

    return answer

