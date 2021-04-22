from sys import stdin
from _collections import deque
from copy import deepcopy

dy = (1,0,-1,0)
dx = (0,1,0,-1)

M, N, K = map(int, stdin.readline().split())
board = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

visited = deepcopy(board)
answer = 0

def bfs(x, y, visited):
    global answer
    visit = deque([(x,y)])
    count = 1
    while visit:
        i, j = visit.popleft()

        for n in range(4):
            nx, ny = i + dx[n], j + dy[n]

            if 0<= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                visit.append((nx,ny))
                count += 1
    answer += 1
    return visited, count

result = []
for i in range(N):
    for j in range(M):
        
        if visited[i][j] == 0:
            visited[i][j] = 1
            visited, count = bfs(i,j,visited)
            result.append(count)
result.sort()
result = [str(i) for i in result]
print(answer)
print(" ".join(result))