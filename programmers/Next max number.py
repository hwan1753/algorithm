def solution(n):
    arr = [] # n을 2진수로 변환
    res = [] # n 다음 숫자의 2진수

    # n 숫자를 2진수로 변환
    while n >= 2:
        if n % 2 == 0:
            arr.append(0)
        else:
            arr.append(1)
        n = n // 2
    arr.append(1)



    tmp = [] # 임의의 배열
    zero, one = 0,0 #
    val = 1 #
    result = 0 # 결과값.

    # n의 2진수로부터 시작
    for idx in range(len(arr)-1):
        k = arr[idx]

        # 만약 해당 값이 1이고 그 다음 값이 0인 경우 서로 변경.
        if k == 1 and arr[idx+1] == 0:
            # zero와 one을 이용하여 바꾼 부분 뒤를 가장 작은 수로 만듬.
            for i in range(one):
                res.append(1)
            for j in range(zero):
                res.append(0)

            res.append(arr[idx+1]) # 1과 0을 서로 변경.
            res.append(1)

            # 나머지 부분을 합침.
            res.extend(arr[idx+2:])

            # 2진수 -> 10진수
            for x in res:
                result += val * x
                val *= 2
            return result

        # 바꾸기 전의 1의 갯수
        elif k == 1:
            one += 1

        # 바꾸기 전의 0의 갯수
        elif k == 0:
           zero += 1

    # 만약 위에서 return이 안된 경우, 더이상 바꾸는 것으로 증가 안되는 경우
    for j in range(one):
        tmp.append(1)
    for i in range(zero):
        tmp.append(0)

    # 2번째에 0을 추가하여 1의 갯수도 같으면서 다음 큰 수
    tmp.append(0)
    tmp.append(1)

    for x in tmp:
        result += val * x
        val *= 2
    return result




a = 6
print(solution(a))