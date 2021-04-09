from sys import stdin
from _collections import deque
import heapq

N, M = map(int, stdin.readline().split())
node_dict = {i:[] for i in range(M+1)}
for _ in range(N):
    start, end, distance = map(int, stdin.readline().split())

    if end <= M:
        node_dict[start] += [(end, distance)]



visit = [(0,0)]
visited = [1e9]*(M+1)
visited[0] = 0

while visit and visited[M] == 1e9:
    now_spend, loc = heapq.heappop(visit)
    # now_spend = visited[loc]
    print(now_spend, loc)
    
    for end, weight in node_dict[loc]:
        
        if visited[end] > now_spend + weight and end-loc > weight:
            heapq.heappush(visit, (now_spend+weight, end))
            visited[end] = now_spend + weight
    
    heapq.heappush(visit, (now_spend+1, loc+1))
    visited[loc+1] = now_spend+1

print(visited[M])