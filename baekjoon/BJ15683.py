from sys import stdin

Up, Right, Down, Left = 0,1,2,3
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def watch(y, x, direction):
    res_set = set()

    for di in direction:
        ny, nx = y, x
        while True:
            ny += dy[di]
            nx += dx[di]
            if 0 <= ny < N and 0 <= nx < M:

                if matrix[ny][nx] == 0:
                    res_set.add((ny, nx))
                elif matrix[ny][nx] == 6:
                    break
            else:
                break
    return res_set

def dfs(i, set_wall):
    global max_wall

    if i == len(all_case):
        if max_wall < len(set_wall):
            max_wall = len(set_wall)

        # return
    else:
        for n in all_case[i]:
            dfs(i+1, set_wall.union(n))


N, M = map(int, stdin.readline().split())

matrix = [list(map(int,stdin.readline().split())) for _ in range(N)]

all_case = []
empty = 0

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 0:
            empty += 1
        elif matrix[y][x] == 1:
            all_case.append([watch(y,x,[Up]),watch(y,x,[Right]),watch(y,x,[Down]),watch(y,x,[Left])])
        elif matrix[y][x] == 2:
            all_case.append([watch(y,x,[Up,Down]),watch(y,x,[Right,Left])])
        elif matrix[y][x] == 3:
            all_case.append([watch(y,x,[Up,Right]),watch(y,x,[Right,Down]),watch(y,x,[Down,Left]),watch(y,x,[Left,Up])])
        elif matrix[y][x] == 4:
            all_case.append([watch(y,x,[Up,Right,Down]),watch(y,x,[Right,Down,Left]),watch(y,x,[Down,Left,Up]),watch(y,x,[Left,Up,Right])])
        elif matrix[y][x] == 5:
            all_case.append([watch(y,x,[Up,Right,Down,Left])])

max_wall = 0
dfs(0, set())
print(empty - max_wall)