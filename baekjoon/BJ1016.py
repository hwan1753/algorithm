from sys import stdin
import math

min_, max_ = map(int, stdin.readline().split())
count = max_ - min_ + 1
answer = 0

dp = [1] * count
N = 2

while N * N <= max_:
    
    square = N * N
    i = min_ // square

    while square * i <= max_:
        idx = square * i - min_

        if idx >= 0 and dp[idx]:
            answer += 1
            dp[idx] = 0
        i += 1
    N += 1
else:
    print(dp.count(1))