def solution(n):
    ans = 0

    while n > 0:
        calculation = 1
        while n >= calculation:
            tmp = calculation
            calculation = calculation * 2

        n -= tmp
        ans += 1

    return ans

a = 5
b = 6
c = 5000
print(solution(c))
