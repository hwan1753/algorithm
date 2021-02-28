def solution(n, times):
    answer = 0      # 정답값
    start = 1       # 최소 시작
    end = n * max(times)    # 최대 시작

    # 이분탐색 시작
    while start <= end:
        middle = (start + end) // 2

        # 해당 시간 동안 몇 명을 심사할 수 있는지
        count = 0
        for time in times:
            count += middle // time

        # n명 이상인 경우 end값 조정
        if count >= n:
            answer = middle
            end = middle - 1
        # n명 미만인 경우 start값 조정
        else:
            start = middle + 1
    return answer