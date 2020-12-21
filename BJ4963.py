from sys import stdin
from _collections import deque

dy = (-1,-1,-1,0,1,1,1,0)
dx = (-1,0,1,1,1,0,-1,-1)

while True:
    w, h = map(int,stdin.readline().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, stdin.readline().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    queue = deque()
    answer = 0

    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = 1

                for n in range(len(dy)):
                    ny, nx = y + dy[n], x + dx[n]
                    if 0 <= ny < h and 0 <= nx < w:
                        if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                            queue.append((ny,nx))
                            visited[ny][nx] = 1

                while queue:
                    qy, qx = queue.popleft()

                    for n in range(len(dy)):
                        ny, nx = qy + dy[n], qx + dx[n]
                        if 0 <= ny < h and 0 <= nx < w:
                            if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                                queue.append((ny, nx))
                                visited[ny][nx] = 1
                answer += 1
    print(answer)
