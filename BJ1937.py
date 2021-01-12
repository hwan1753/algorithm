from sys import stdin
import heapq
from itertools import chain

dy = [-1,0,1,0]
dx = [0,-1,0,1]

n = int(stdin.readline())

matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
memoization = [[0] * n for _ in range(n)]
heap = []

for y in range(n):
    for x in range(n):
        heapq.heappush(heap, (-1 * matrix[y][x], y, x))



while heap:
    _, y, x = heapq.heappop(heap)
    chk_arr = []

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if matrix[y][x] < matrix[ny][nx]:
                chk_arr.append(memoization[ny][nx])
    if chk_arr:
        memoization[y][x] = max(chk_arr) + 1
    else:
        memoization[y][x] = 1

print(max(chain(*memoization)))