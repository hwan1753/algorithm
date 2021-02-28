from sys import stdin
from _collections import deque

dy = [1,-1,0,0]
dx = [0,0,1,-1]

N = int(stdin.readline())
matrix = []


for n in range(N):
    aa = list(map(int,stdin.readline().split()))
    matrix.append(aa)
island = [[0] * N for _ in range(N)]

i_queue = deque()

id = 1

minimum = 9999
for my in range(N):
    for mx in range(N):
        beach = [[0] * N for _ in range(N)]
        i_visited = [[0] * N for _ in range(N)]
        d_queue = deque()

        if matrix[my][mx] == 1 and island[my][mx] == 0:
            island[my][mx] = id
            i_queue.append((my,mx))
            i_visited[my][mx] = 1

            while i_queue:
                y, x = i_queue.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        if matrix[ny][nx] == 1 and i_visited[ny][nx] == 0:
                            island[ny][nx] = id
                            i_queue.append((ny,nx))
                            i_visited[ny][nx] = 1
                        elif matrix[ny][nx] == 0:
                            beach[ny][nx] = 1
                            i_visited[ny][nx] = 1
                            d_queue.append((ny,nx))

            d_stop = False
            while d_queue:
                if d_stop == True:
                    break
                y, x = d_queue.popleft()
                for k in range(4):
                    by = y + dy[k]
                    bx = x + dx[k]
                    if 0 <= by < N and 0 <= bx < N:
                        if matrix[by][bx] == 0 and i_visited[by][bx] == 0:
                            beach[by][bx] = beach[y][x] + 1
                            i_visited[by][bx] = 1
                            d_queue.append((by,bx))
                        elif matrix[by][bx] == 1 and i_visited[by][bx] == 0:
                            if minimum > beach[y][x]:
                                minimum = beach[y][x]

                            d_stop = True
                            break

            id += 1

print(minimum)