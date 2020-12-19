from sys import stdin

matrix = []
N, M, y, x, K = map(int, stdin.readline().split())
for n in range(N):
    matrix.append(list(map(int,stdin.readline().split())))

command = list(map(int,stdin.readline().split()))

dice = [0 for _ in range(6)]

for act in command:

    temp_dice = [0 for _ in range(6)]
    if act == 1:
        if x == M-1:
            continue
        else:
            x += 1
            temp_dice[0] = dice[3]
            temp_dice[1] = dice[1]
            temp_dice[2] = dice[0]
            temp_dice[3] = dice[5]
            temp_dice[4] = dice[4]
            temp_dice[5] = dice[2]
            if matrix[y][x] == 0:

                matrix[y][x] = dice[2]
            else:
                temp_dice[5] = matrix[y][x]
                matrix[y][x] = 0
            print(temp_dice[0])


    elif act == 2:
        if x == 0:
            continue
        else:
            x -= 1
            temp_dice[0] = dice[2]
            temp_dice[1] = dice[1]
            temp_dice[2] = dice[5]
            temp_dice[3] = dice[0]
            temp_dice[4] = dice[4]
            temp_dice[5] = dice[3]
            if matrix[y][x] == 0:

                matrix[y][x] = dice[3]
            else:
                temp_dice[5] = matrix[y][x]
                matrix[y][x] = 0
            print(temp_dice[0])

    elif act == 3:

        if y == 0:
            continue
        else:
            y -= 1
            temp_dice[0] = dice[4]
            temp_dice[1] = dice[0]
            temp_dice[2] = dice[2]
            temp_dice[3] = dice[3]
            temp_dice[4] = dice[5]
            temp_dice[5] = dice[1]
            if matrix[y][x] == 0:

                matrix[y][x] = dice[1]
            else:
                temp_dice[5] = matrix[y][x]
                matrix[y][x] = 0
            print(temp_dice[0])
    elif act == 4:
        if y == N -1:
            continue
        else:
            y += 1
            temp_dice[0] = dice[1]
            temp_dice[1] = dice[5]
            temp_dice[2] = dice[2]
            temp_dice[3] = dice[3]
            temp_dice[4] = dice[0]
            temp_dice[5] = dice[4]
            if matrix[y][x] == 0:

                matrix[y][x] = dice[4]
            else:
                temp_dice[5] = matrix[y][x]
                matrix[y][x] = 0
            print(temp_dice[0])

    dice = temp_dice.copy()