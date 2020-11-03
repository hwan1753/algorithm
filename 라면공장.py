# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies),
# 원래 공장으로부터 공급받을 수 있는 시점 k
def solution(stock, dates, supplies, k):

    idx = 0
    answer = 0

    while stock < k - 2:
        day = 0
        for num in range(idx,len(dates)):
            day += dates[num]
            if day > stock - 1:

                k -= stock
                stock = supplies[num]
                idx = num + 1
                answer += 1

                print(idx, k, stock)
                break


        print(answer)

    return answer

a = 4
b = [4,10,15]
c = [20,5,10]
d = 30
solution(a,b,c,d)