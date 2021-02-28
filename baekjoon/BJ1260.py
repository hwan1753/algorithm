import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    # 입력값 매트릭스로 구현
    line = list(map(int,sys.stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

# DFS 구현
def dfs(start, visited):
    # stack 활용
    visited += [start]
    for c in range(len(matrix[start])):
        # start에서 c로 갈 수 있으면서 아직 방문하지 않은 경우에 방문.
        if matrix[start][c] == 1 and c not in visited:
            dfs(c,visited)
    return visited

# BFS 구현
def bfs(start):
    # Queue로 구현
    visited = [start]
    queue = deque([start])

    while queue:
        # popleft로 0에 값 뽑기
        n = queue.popleft()
        for c in range(len(matrix[start])):
            # n에서 c로 갈 수 있으면서 아직 방문하지 않은 경우에 방문.
            if matrix[n][c] == 1 and c not in visited:

                visited.append(c)   # 방문처리
                queue.append(c)     # Queue에 추가
    return visited

print(*dfs(v,[]))
print(*bfs(v))