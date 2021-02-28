from sys import stdin
from _collections import deque

def move_bfs(shark):

    shark_size, shark_y, shark_x = shark[0], shark[1], shark[2]
    visited[shark_y][shark_x] = 1
    for i in range(4):

        if 0 <= shark_y + dy[i] <= N-1 and 0 <= shark_x + dx[i] <= N-1:
            if matrix[shark_y + dy[i]][shark_x + dx[i]] > shark_size:
                pass
            elif matrix[shark_y + dy[i]][shark_x + dx[i]] < shark_size and matrix[shark_y + dy[i]][shark_x + dx[i]] != 0:
                # matrix[shark_y + dy[i]][shark_x + dx[i]] = 0
                return [shark_size, shark_y + dy[i], shark_x + dx[i]]

            elif visited[shark_y + dy[i]][shark_x + dx[i]] == 0:
                visit2.append([shark_y + dy[i], shark_x + dx[i]])
                visited[shark_y + dy[i]][shark_x + dx[i]] = 1




N = int(stdin.readline())

shark = [2]
matrix = []

visit1 = deque([])
visit2 = deque([])

visited = [[0] * N for _ in range(N)]
answer, time = 0, 0
# print(visited)
dy = [-1,0,0,1]
dx = [0,-1,1,0]

for y in range(N):
    fish_arr = list(map(int, stdin.readline().split()))
    matrix.append(fish_arr)

    for x in range(len(fish_arr)):
        if fish_arr[x] == 9:
            shark.append(y)
            shark.append(x)
            # print(y,x)
            visited[y][x] = 1

chk = None
count = 0
temp_shark = shark.copy()

while True:
    can_shark = []
    # print(temp_shark)
    chk = move_bfs(temp_shark)

    if chk:
        can_shark.append(chk)
        while visit1:
            vi = visit1.popleft()
            temp_shark[1], temp_shark[2] = vi[0], vi[1]
            chk = move_bfs(temp_shark)
            if chk:
                can_shark.append(chk)

        minimum = [99,99]
        # print(can_shark)

        for c in can_shark:
            if minimum[0] > c[1]:
                minimum = [c[1],c[2]]
            elif minimum[0] == c[1] and minimum[1] > c[2]:
                minimum = [c[1],c[2]]

        temp_shark[1], temp_shark[2] = minimum[0], minimum[1]

        count += 1
        if count % temp_shark[0] == 0:
            temp_shark[0] += 1
            count = 0

        visit2 = deque([])
        visited = [[0] * N for _ in range(N)]
        time += 1
        # print(temp_shark,count, time)
        matrix[shark[1]][shark[2]] = 0
        matrix[temp_shark[1]][temp_shark[2]] = 0
        visited[temp_shark[1]][temp_shark[2]] = 1

        chk = None
        answer = time

    elif visit1:
        vi = visit1.popleft()
        temp_shark[1], temp_shark[2] = vi[0], vi[1]
    elif visit2:
        visit1 = visit2.copy()
        visit2 = deque([])
        vi = visit1.popleft()
        temp_shark[1], temp_shark[2] = vi[0], vi[1]
        time += 1

    else:
        print(answer)
        break