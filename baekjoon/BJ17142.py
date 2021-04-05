from sys import stdin
from _collections import deque
from itertools import chain
from pprint import pprint

def comb(lst, num):

    arr =[]
    if num > len(lst):
        return arr

    if num == 1:
        for i in lst:
            arr.append([i])
    
    else:
        for i in range(len(lst)-num+1):
            for temp in comb(lst[i+1:],num-1):
                arr.append([lst[i]]+temp)
    
    return arr


n, m = map(int, stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(n)]

dy = (0,1,0,-1)
dx = (1,0,-1,0)

virus = []
wall = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i,j))
        
        if board[i][j] == 1:
            wall.append((i,j))

candidate_arr = comb(virus, m)
answer = 1e9

if list(chain(*board)).count(0) == 0:
    answer = 0
    candidate_arr = []

for candidate in candidate_arr:
    visit = deque(candidate)
    visited = [[1e9]*n for _ in range(n)]
    for i, j in candidate:
        visited[i][j] = 0
    for i, j in wall:
        visited[i][j] = -1

    temp = 0

    while visit:
        y, x = visit.popleft()
        weight = visited[y][x]

        
        for i in range(4):
            my, mx = y + dy[i], x + dx[i]

            if 0<=my<n and 0<=mx<n:

                if board[my][mx] == 2 and visited[my][mx] == 1e9:
                    visited[my][mx] = weight + 1
                    visit.append((my,mx))

                elif board[my][mx] == 1:
                    visited[my][mx] = -1

                elif visited[my][mx] > weight+1:
                    visited[my][mx] = weight + 1
                    visit.append((my,mx))
                    temp = max(temp, visited[my][mx])
    
    if list(chain(*visited)).count(1e9):
        pass
    else:
        answer = min(answer, temp)


if answer == 1e9:
    print(-1)
else:
    print(answer)
