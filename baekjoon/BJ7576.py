from sys import stdin
from _collections import deque

M, N = map(int,stdin.readline().split())
matrix = [list(map(int,stdin.readline().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]


visited = [[0] * M for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
idx = 0
queue = deque()
value = 0
start = []
for n in range(N):
    for m in range(M):
        if matrix[n][m] == 1:
            start.append((n,m))
            queue.append((n,m))
            visited[n][m] = 1
            dist[n][m] = 0
        elif matrix[n][m] == -1:
            dist[n][m] = 0




# while idx < len(start):
while queue:
    y, x = queue.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[ny][nx] == 0 and visited[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = 1
                dist[ny][nx] = dist[y][x] + 1

stop = False
maximum = 0
for n in range(N):
    if stop == False:
        for m in range(M):
            if dist[n][m] == -1:
                stop = True
                break
            else:
                if dist[n][m] > maximum:
                    maximum = dist[n][m]
    else:
        break
if stop == False:
    print(maximum)
else:
    print(-1)