from sys import stdin
from _collections import deque

N = int(stdin.readline())
K = int(stdin.readline())

apple = []
for k in range(K):
    apple.append(tuple(map(int,stdin.readline().split())))


L = int(stdin.readline())
command = deque([])
for l in range(L):
    command.append(tuple(stdin.readline().split()))

snake = deque([[1,1]])
change = []
time = 0

direct = 1
while True:
    time += 1
    head = snake[0]
    if direct == 1:

        if head[1] + 1 > N or [head[0],head[1]+1] in snake:
            print(time)
            break
        elif (head[0],head[1] + 1) in apple:
            snake.appendleft([head[0],head[1]+1])
            apple.remove((head[0],head[1]+1))
        else:
            snake.appendleft([head[0],head[1]+1])
            snake.pop()

    elif direct == 2:
        if head[0] + 1 > N or [head[0]+1,head[1]] in snake:
            print(time)
            break
        elif (head[0]+1,head[1]) in apple:
            snake.appendleft([head[0]+1,head[1]])
            apple.remove((head[0]+1,head[1]))
        else:
            snake.appendleft([head[0]+1,head[1]])
            snake.pop()

    elif direct == 3:
        if head[1] - 1 < 1 or [head[0],head[1]-1] in snake:
            print(time)
            break
        elif (head[0],head[1] - 1) in apple:
            snake.appendleft([head[0],head[1]-1])
            apple.remove((head[0],head[1]-1))
        else:
            snake.appendleft([head[0],head[1]-1])
            snake.pop()

    elif direct == 0:
        if head[0] - 1 < 1 or [head[0]-1,head[1]] in snake:
            print(time)
            break
        elif (head[0]-1,head[1]) in apple:
            snake.appendleft([head[0]-1,head[1]])
            apple.remove((head[0]-1,head[1]))
        else:
            snake.appendleft([head[0]-1,head[1]])
            snake.pop()

    if command:
        if time == int(command[0][0]):
            if command[0][1] == "L":
                if direct == 0:
                    direct = 3
                else:
                    direct -= 1

            elif command[0][1] == "D":
                direct += 1
                direct = direct % 4
            # print(direct, command[0])
            command.popleft()

    # print(snake, time)
