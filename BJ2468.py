from sys import stdin

N = int(stdin.readline())

dy = [-1,0,1,0]
dx = [0,-1,0,1]

matrix = []
for _ in range(N):
    matrix.append(list(map(int, stdin.readline().split())))

def dfs(h):
    stack = []
    visited = [[0] * N for _ in range(N)]
    result = 0

    for y in range(N):
        for x in range(N):
            if matrix[y][x] > h and visited[y][x] == 0:
                stack.append((y,x))
                visited[y][x] = 1
                result += 1
                while stack:
                    ny, nx = stack.pop()
                    # print(ny, nx)
                    for i in range(4):
                        cy = ny + dy[i]
                        cx = nx + dx[i]
                        if 0 <= cy < N and 0 <= cx < N:
                            if matrix[cy][cx] > h and visited[cy][cx] == 0:
                                stack.append((cy,cx))
                                visited[cy][cx] = 1
                # print(h)
                # for a in visited:
                #     print(visited)
    return result

maximum = -1

for i in range(101):
    answer = dfs(i)
    # print(answer)
    if answer > maximum:
        maximum = answer
    elif answer == 0:
        break
print(maximum)