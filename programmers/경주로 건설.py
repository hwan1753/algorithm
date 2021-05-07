from _collections import deque
from pprint import pprint

dy = (0,1,0,-1)
dx = (1,0,-1,0)

def solution(board):
    answer = 0

    visit = deque([[0,0,0,0],[0,0,1,0]])
    visited = [[1e9]*len(board) for _ in range(len(board))]
    visited[0][0] = 0

    while visit:
        y, x, direct, weight = visit.popleft()
        
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if 0<=ny<len(board) and 0<=nx<len(board) and board[ny][nx] != 1:
                if direct == i and weight + 100 <= visited[ny][nx]:
                    visited[ny][nx] = weight + 100
                    visit.append([ny,nx,i, weight + 100])
                elif direct != i and weight + 600 <= visited[ny][nx] + 500:
                    if weight + 600 <= visited[ny][nx]:
                        visited[ny][nx] = weight + 600
                    visit.append([ny,nx,i, weight+600])
    
    # pprint(visited)
    return visited[-1][-1]


b = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [1,0,0,0,1],
    [0,1,1,0,0]
]
print(solution(b))