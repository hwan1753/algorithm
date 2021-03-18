from sys import stdin

N, M = map(int, stdin.readline().split())

num_arr = list(map(int, stdin.readline().split()))
dp = [0] * (N+1)
dp[1] = num_arr[0]
for i in range(2,N+1):
    dp[i] += dp[i-1] + num_arr[i-1]

for _ in range(M):
    start, end = map(int, stdin.readline().split())
    print(dp[end] - dp[start-1])