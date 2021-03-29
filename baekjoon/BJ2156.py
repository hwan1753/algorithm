from sys import stdin

n = int(stdin.readline())

num_arr = [0] + [int(stdin.readline()) for _ in range(n)]

dp = [0] * (n+1)
dp[1] = num_arr[1]

if n > 1:
    dp[2] = dp[1] + num_arr[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + num_arr[i], dp[i-3] + num_arr[i-1] + num_arr[i])

print(dp[-1])
