from sys import stdin
from _collections import deque
import heapq

V, E = map(int,stdin.readline().split())
K = int(stdin.readline())
node_dict = {}

for v in range(1,V+1):
    node_dict[v] = []

for e in range(E):
    start, end, weight = map(int,stdin.readline().split())
    node_dict[start] += [(end, weight)]

# for node in node_dict:
#     node_dict[node].sort(reverse=True, key=lambda x:x[1])

# print(node_dict)

visited = [99999999] * (V+1)
visited[K] = 0
heap = []
heapq.heappush(heap,[0,K])
while heap:
    weight, now = heapq.heappop(heap)
    for node in node_dict[now]:
        if visited[node[0]] > weight + node[1]:
            visited[node[0]] = weight + node[1]
            heapq.heappush(heap, [visited[node[0]], node[0]])
for i in range(1,V+1):
    if visited[i] == 99999999:
        print("INF")
    else:
        print(visited[i])