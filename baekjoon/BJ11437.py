from sys import stdin
import sys
from functools import lru_cache


sys.setrecursionlimit(10 ** 5)

N = int(input())

# graph = [[] for _ in range(N+1)]  # 그래프 정보
graph = {i:[] for i in range(1,N+1)}
depth = [0] * (N+1)             # 깊이 정보
chk = [0] * (N+1)               # 계산 여부 정보
parent = [0] * (N+1)            # 부모 정보

for i in range(N-1):
    num_a, num_b = map(int, input().split())
    graph[num_a].append(num_b)
    graph[num_b].append(num_a)

# 노드 깊이 계산
# @lru_cache(maxsize=64)
def dfs(x, num):
    chk[x] = 1
    
    for i in graph[x]:
        if chk[i]:
            continue
        depth[i] = num+1
        parent[i] = x
        dfs(i, num+1)

dfs(1, 0)

# def lca(a,b):
#     while depth[a] != depth[b]:
#         if depth[a] < depth[b]:
#             b = parent[b]
#         else:
#             a = parent[a]
    
#     while a != b:
#         a = parent[a]
#         b = parent[b]
#     return a


M = int(input())
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    while depth[a] != depth[b]:
        if depth[a] < depth[b]:
            b = parent[b]
        else:
            a = parent[a]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)