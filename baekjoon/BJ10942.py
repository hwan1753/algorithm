from sys import stdin

N = int(stdin.readline())

num_arr = [0] + list(map(int, stdin.readline().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, len(num_arr)):
    dp[i][i] = 1

for i in range(N):
    if num_arr[i] == num_arr[i+1]:
        dp[i][i+1] = 1

for i in range(2,N+1):
    for j in range(N+1-i):
        if num_arr[j] == num_arr[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

for _ in range(int(stdin.readline())):
    start, end = map(int, stdin.readline().split())
    print(dp[start][end])
