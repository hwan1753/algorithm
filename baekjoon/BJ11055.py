from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())

num_arr = list(map(int, stdin.readline().split()))
answer = 0
dp = num_arr[:]

for i in range(N):
    for j in range(i):

        if num_arr[i] > num_arr[j]:
            dp[i] = max(dp[i], dp[j]+num_arr[i])

# print(dp)
print(max(dp))
