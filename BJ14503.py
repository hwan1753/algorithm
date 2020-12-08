from sys import stdin

r, c = map(int, stdin.readline().split())
y, x, front = map(int, stdin.readline().split())

if front == 1:
    front = 3
elif front == 3:
    front = 1

direction = [[-1,0],[0,-1],[1,0],[0,1]]


matrix = []

for row in range(r):
    matrix.append(list(map(int, stdin.readline().split())))

all_direct = 0
answer = 1
matrix[y][x] = 2

while True:
    if all_direct == 4:
        if matrix[y - direction[front][0]][x - direction[front][1]] == 1:
            break
        else:

            y = y - direction[front][0]
            x = x - direction[front][1]
            all_direct = 0


    front = (front + 1) % 4

    check_y = y + direction[front][0]
    check_x = x + direction[front][1]
    # 가장자리 벽 안쪽

    if matrix[check_y][check_x] == 0:
        # print(check_y, check_x)
        matrix[check_y][check_x] = 2
        y, x = check_y, check_x
        all_direct = 0
        answer += 1
    else:

        all_direct += 1

print(answer)