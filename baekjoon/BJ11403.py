from sys import stdin
from _collections import deque

def bfs(i, N, matrix):

    visited = [0] * N
    visit = deque([i])

    while visit:
        edge = visit.popleft()
        
        for x in range(N):
            if matrix[edge][x] == 1 and visited[x] == 0:
                visit.append(x)
                visited[x] = 1
    return visited

N = int(stdin.readline())

matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = []

for i in range(N):
    answer.append(bfs(i,N,matrix))
# print('---------------------------')
for i in answer:
    ans = " ".join(str(j) for j in i)
    print(ans)