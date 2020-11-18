def solution(n):
    arr = []
    res = []
    while n >= 2:
        if n % 2 == 0:
            arr.append(0)
        else:
            arr.append(1)
        n = n // 2

    arr.append(1)
    # arr = deque(reversed(arr))
    # print(arr)


    tmp = []
    zero, one = 0,0
    val = 1
    result = 0
    # while arr:
    for idx in range(len(arr)-1):
        k = arr[idx]

        if k == 1 and arr[idx+1] == 0:
            for i in range(one):
                res.append(1)
            for j in range(zero):
                res.append(0)

            res.append(arr[idx+1]) # 자리바꾸는 1 앞에 0
            res.append(1)

            res.extend(arr[idx+2:])
            # print(res)
            for x in res:
                result += val * x
                val *= 2
            return result

        elif k == 1:
            one += 1

        elif k == 0:
           zero += 1


    for j in range(one):
        tmp.append(1)
    for i in range(zero):
        tmp.append(0)

    tmp.append(0)
    tmp.append(1)

    for x in tmp:
        result += val * x
        val *= 2
    return result




a = 6
print(solution(a))