from sys import stdin
from _collections import deque

N = int(stdin.readline())
matrix = [list(map(int,input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0] * N for _ in range(N)]
queue = deque()
result = 0
result_list = []
X, Y = 0, 0
# print(matrix)
while Y < N:
    x, y = X, Y
    # print("y, x : {}, {}".format(y, x))
    # print(matrix[y][x])
    if matrix[y][x] == 0 or visited[y][x] != 0:
        if X < N-1:
            X += 1
        else:
            Y += 1
            X = 0
    else:
        value = 1
        visited[y][x] = 1
        # print(queue)
        queue.append((y,x))
        while queue:
            y, x = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                # print("y, x : {}, {}".format(ny, nx))
                if 0 <= nx < N and 0 <= ny < N:

                    if visited[ny][nx] == 0 and matrix[ny][nx] == 1:
                        visited[ny][nx] = 1
                        queue.append((ny,nx))
                        value += 1
                        # print("y, x : {}, {}!!".format(ny, nx))
                        # print("!!")
        result += 1
        result_list.append(value)
        if X < N-1:
            X += 1
        else:
            Y += 1
            X = 0
print(result)
# print(result_list)
for v in sorted(result_list):
    print(v)