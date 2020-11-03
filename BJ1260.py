import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    line = list(map(int,sys.stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1
# for a in matrix:
#     print(a)

def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and c not in visited:
            dfs(c,visited)
    return visited

def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        n = queue.popleft()
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and c not in visited:
                visited.append(c)
                queue.append(c)
    return visited

print(*dfs(v,[]))
print(*bfs(v))