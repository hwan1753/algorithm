def solution(baseball):
    num_list = []
    for one in range(1,10):
        for two in range(1,10):
            if one == two:
                pass
            else:
                for three in range(1,10):
                    if one == three or two == three:
                        pass
                    else:
                        num_list.append([one,two,three])
    # print(num_list)
    result = 0
    for chk in num_list:
        stop = False
        for st in baseball:

            num = st[0]
            strike = 0
            ball = 0

            num1 = num // 100
            num2 = (num // 10) % 10
            num3 = num % 10

            cor = [num1,num2,num3]
            for id in range(3):
                if chk[id] == cor[id]:
                    strike += 1
                else:
                    if chk[id] in cor:
                        ball += 1
            if strike == st[1] and ball == st[2]:
                pass
            else:
                stop = True
                break
        if stop == False:
            result += 1
    return result




a = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
b = [[356, 1, 0], [327, 2, 0], [489, 0, 0]]
solution(a)
