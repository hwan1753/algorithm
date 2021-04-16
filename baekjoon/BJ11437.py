from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)

N = int(stdin.readline())

graph = [[] for _ in range(N+1)]  # 그래프 정보
depth = [0] * (N+1)             # 깊이 정보
chk = [0] * (N+1)               # 계산 여부 정보
parent = [0] * (N+1)            # 부모 정보

for i in range(N-1):
    num_a, num_b = map(int, stdin.readline().split())
    graph[num_a].append(num_b)
    graph[num_b].append(num_a)

# 노드 깊이 계산
def dfs(x, num):
    chk[x] = 1
    depth[x] = num
    for i in graph[x]:
        if chk[i]:
            continue

        parent[i] = x
        dfs(i, num+1)

dfs(1, 1)

def lca(a,b):
    if depth[a] < depth[b]:
        while depth[a] == depth[b]:
            b = parent[b]


M = int(stdin.readline())
for _ in range(M):
