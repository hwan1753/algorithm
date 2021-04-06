from sys import stdin
from itertools import chain
from pprint import pprint

r, c, t = map(int, stdin.readline().split())

board = [list(map(int, stdin.readline().split())) for _ in range(r)]

machine = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            machine.append((i,j))


def dust(board):
    temp = [[0]*c for _ in range(r)]

    dy = (0,1,0,-1)
    dx = (1,0,-1,0)

    for i in range(r):
        for j in range(c):

            if board[i][j] >= 0:
                val = board[i][j] // 5
                num = board[i][j]
                for k in range(4):
                    my, mx = i+dy[k], j+dx[k]

                    if 0<=my<r and 0<=mx<c and board[my][mx] >= 0:
                        temp[my][mx] += val
                        num -= val
                    
                temp[i][j] += num

            else:
                temp[i][j] = -1
    return temp

def running(one, two, board):

    dy1 = (-1, 0, 1, 0)
    dx1 = (0, 1, 0, -1)

    dy2 = (1, 0, -1, 0)
    dx2 = (0, 1, 0, -1)

    
    idx = 0
    i, j= one
    my, mx = i, j
    

    while idx < 4:
            
        my += dy1[idx]
        mx += dx1[idx]
        if 0<=my+dy1[idx]<=i and 0<=mx+dx1[idx]<c and board[my+dy1[idx]][mx+dx1[idx]] >= 0:
            board[my][mx] = board[my+dy1[idx]][mx+dx1[idx]]
        else:
            idx += 1
            if my == i and mx-1 == j:
                board[my][mx] = 0
                break
            else:
                
                board[my][mx] = board[my+dy1[idx]][mx+dx1[idx]]


    idx = 0
    i, j= two
    my, mx = i, j
    

    while idx < 4:
            
        my += dy2[idx]
        mx += dx2[idx]
        
        if i<=my+dy2[idx]<r and 0<=mx+dx2[idx]<c and board[my+dy2[idx]][mx+dx2[idx]] >= 0:
            board[my][mx] = board[my+dy2[idx]][mx+dx2[idx]]
        else:
            idx += 1
            if my == i and mx-1 == j:
                board[my][mx] = 0
                break
            else:
                
                board[my][mx] = board[my+dy2[idx]][mx+dx2[idx]]

    return board


for _ in range(t):
    board = dust(board)
    board = running(machine[0], machine[1], board)

print(sum(list(chain(*board)))+2)