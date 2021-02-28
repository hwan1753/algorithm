from sys import stdin
from _collections import deque

N, M = map(int,stdin.readline().split())
matrix = [list(map(int,stdin.readline().split())) for _ in range(N)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

virus = []
wall = []
exist = []

for n in range(N):
    for m in range(M):
        if matrix[n][m] == 2:
            virus.append((n,m))
        elif matrix[n][m] == 0:
            wall.append([n,m])
        else:
            exist.append([n,m])



idx = 0
result = -1
for a in range(len(wall)):
    for b in range(a+1,len(wall)):
        if a != b:
            for c in range(b+1,len(wall)):
                if a == c or b == c:
                    pass
                else:
                    queue = deque(a for a in virus)
                    visited = [[0] * M for _ in range(N)]
                    for ww in range(len(exist)):
                        visited[exist[ww][0]][exist[ww][1]] = 1
                    visited[wall[a][0]][wall[a][1]] = 1
                    visited[wall[b][0]][wall[b][1]] = 1
                    visited[wall[c][0]][wall[c][1]] = 1
                    value = 0
                    # print(wall[a],wall[b],wall[c])
                    matrix[wall[a][0]][wall[a][1]] = 1
                    matrix[wall[b][0]][wall[b][1]] = 1
                    matrix[wall[c][0]][wall[c][1]] = 1
                    while queue:
                        y, x = queue.popleft()
                        visited[y][x] = 1
                        for k in range(4):
                            ny = y + dy[k]
                            nx = x + dx[k]
                            if 0 <= ny < N and 0 <= nx < M:
                                if matrix[ny][nx] == 0 and visited[ny][nx] == 0:
                                    queue.append((ny,nx))
                                    visited[ny][nx] = 1

                    for ch in visited:
                        for chk in ch:
                            if chk == 0:
                                value += 1
                    if value > result:
                        result = value


                    matrix[wall[a][0]][wall[a][1]] = 0
                    matrix[wall[b][0]][wall[b][1]] = 0
                    matrix[wall[c][0]][wall[c][1]] = 0




print(result)
