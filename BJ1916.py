import heapq
from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

node_dict = {}
for _ in range(M):
    start, end, weight = map(int, stdin.readline().split())
    node_dict[start] = node_dict.get(start, []) + [(end, weight)]

start, final = map(int, stdin.readline().split())

INF = 1e9
visited = [INF] * (N+1)
heap = []
visited[start] = 0
heapq.heappush(heap, (visited[start], start))
while heap:
    weight, now = heapq.heappop(heap)
    if now not in node_dict:
        continue
    for next_node, edge in node_dict[now]:

        if visited[next_node] > weight + edge:
            visited[next_node] = weight + edge
            heapq.heappush(heap, (visited[next_node], next_node))
print(visited[final])