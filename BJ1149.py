from sys import stdin
from _collections import deque

N = int(stdin.readline())

arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = 1e9
queue = deque([])

for n in range(1,N):
    for i in range(3):
        minimum = 1e9

        for j in range(3):
            if i != j and arr[n][i] + arr[n-1][j] < minimum:
                minimum = arr[n][i] + arr[n-1][j]

        arr[n][i] = minimum

print(min(arr[-1]))