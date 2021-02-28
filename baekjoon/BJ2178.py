from _collections import deque

N, M = map(int, input().split())

matrix = [[] for _ in range(N*M + 1)]
large_miro = [list(map(int,list(input()))) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

queue = deque()

queue.append((0,0))
visited[0][0] = 1
dist[0][0] = 1

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and large_miro[nx][ny] == 1:
                queue.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = 1
print(dist[N-1][M-1])