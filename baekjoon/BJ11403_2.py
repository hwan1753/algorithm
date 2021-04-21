from sys import stdin

N = int(stdin.readline())

board = [list(map(int, stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][k] and board[k][j]:
                board[i][j] = 1

# print("-"*10)
for a in board:
    for b in a:
        print(b, end=' ')
    print()