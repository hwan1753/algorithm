from sys import stdin
from _collections import deque

dn = [-1,1,0,0]
dm = [0,0,-1,1]


T = int(stdin.readline())
for tc in range(T):
    M, N, K = map(int,stdin.readline().split())
    matrix = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    target = []
    for k in range(K):
        x, y = map(int,stdin.readline().split())
        target.append((x,y))
        matrix[y][x] = 1
    # for a in matrix:
    #     print(a)
    # print('!!!')
    result = 0
    for tt in range(len(target)):
        if visited[target[tt][1]][target[tt][0]] == 0:
            queue.append(target[tt])
            visited[target[tt][1]][target[tt][0]] = 1
            result += 1
            # print(target[tt])
            while queue:
                a, b = queue.popleft()
                for p in range(4):
                    nx = a + dm[p]
                    ny = b + dn[p]
                    if 0 <= nx < M and 0 <= ny < N:
                        if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            queue.append((nx,ny))
                            # print(nx,ny)
    print(result)
