from sys import stdin
from _collections import deque

def dfs(start,visited,answer):
    for idx in matrix[start]:
        if visited[idx] == 0:
            answer += 1
            visited[idx] = 1
            answer = dfs(idx,visited,answer)
    return answer

N, M = map(int,stdin.readline().split())
matrix = [[] for _ in range(N+1)]


for m in range(M):
    A, B = map(int, stdin.readline().split())
    matrix[B].append(A)

chk = 0
result = []

for n in range(1,1+N):
    visited = [0] * (N + 1)
    visited[n] = 1
    answer = 0
    answer = dfs(n,visited,answer)
    if answer >= chk:
        if answer > chk:
            result = []
        result.append(n)
        chk = answer
print(*result)

# BFS
# for n in range(N):
#     answer = 0
#     visited = [0] * (N + 1)
#     visited[n+1] = 1
#     # print(visited)
#     queue = deque([n+1])
#     stop = False
#     # print(visited)
#     while stop != True:
#
#         if len(queue) == 0:
#             stop = True
#             break
#         else:
#             value = queue.popleft()
#
#         for idx in matrix[value]:
#             if visited[idx] == 0:
#                 queue.append(idx)
#                 visited[idx] = 1
#                 answer += 1
#         # print(queue)
#         # print(visited)
#     if answer >= chk:
#         if answer > chk:
#             result =[]
#         result.append(n+1)
#         chk = answer
#
# print(*result)

