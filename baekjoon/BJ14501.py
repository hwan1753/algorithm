from sys import stdin
import heapq

N = int(stdin.readline())

todo = sorted([[n+1] + list(map(int, stdin.readline().split())) for n in range(N)], reverse=True)

dp = [0] * (N+2)

for idx, day, value in todo:

    if idx + day - 1> N:
        dp[idx] = dp[idx+1]
        continue
    
    dp[idx] = max(value + dp[idx + day], dp[idx+1])


print(dp[1])