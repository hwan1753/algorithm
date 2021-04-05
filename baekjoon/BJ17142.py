from sys import stdin
from _collections import deque

def comb(lst, num):

    arr =[]
    if num > len(lst):
        return arr

    if len(lst) == 1:
        for i in lst:
            arr.append([i])


n, m = map(int, stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(n)]

dy = (0,1,0,-1)
dx = (1,0,-1,0)

chk_arr = []
visit = deque()
visited = [[1e9]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            visit.append((i,j))
            visited[i][j] = 0
        if board[i][j] == 1:
            visited[i][j] = '-'

while visit:
    y, x = visit.popleft()
    weight = visited[y][x]

    
    for i in range(4):
        my, mx = y + dy[i], x + dx[i]

        if 0<=my<n and 0<=mx<n and board[my][mx]