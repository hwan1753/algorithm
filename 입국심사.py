def solution(n, times):
    answer = 0

    start = 1
    end = n * max(times)

    while start <= end:
        middle = (start + end) // 2
        # print(middle)
        count = 0
        for time in times:
            count += middle // time

        if count >= n:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    return answer