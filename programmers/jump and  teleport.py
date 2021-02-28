def solution(n):
    ans = 0     # 결과값

    while n > 0:    # n이 0이 될 때까지
        calculation = 1     # 2의 제곱으로 계산하는 수
        while n >= calculation:     # n보다 작은 2의 제곱
            tmp = calculation       # 가장 큰 2의 제곱 값 저장하기
            calculation = calculation * 2   # 2의 제곱

        n -= tmp    # n보다 작은 가장 큰 2의 제곱 빼주기
        ans += 1    # 결과값 + 1

    return ans      # 결과값 리턴

a = 5
b = 6
c = 5000
print(solution(c))
