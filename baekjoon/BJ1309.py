from sys import stdin

N = int(stdin.readline())

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3

for i in range(2,N+1):
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

# print(dp)
print(dp[-1])