def solution(n):
    add = 0
    answer = 1
    for idx in range(1,n+1):
        add = idx
        for num in range(idx+1,n+1):
            if add + num == n:
                answer += 1
                break
            elif add + num > n:
                break
            elif add + num < n:
                add += num

    return answer

n = 15
print(solution(n))