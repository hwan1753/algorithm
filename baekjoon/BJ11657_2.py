from sys import stdin
from collections import defaultdict, deque
    

N, M = map(int, stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
    start, end, weight = map(int, stdin.readline().split())
    graph[start] += [[end, weight]]

def chk_inf(distance):
    for start in graph:
        for end, weight in graph[start]:
            if distance[start] != 1e9 and distance[end] > distance[start] + weight:
                return False
    return True

distance = [1e9] * (N+1)
distance[1] = 0

for i in range(N-1):
    for start in graph:
        for end, weight in graph[start]:
            
            if distance[start] != 1e9:
                distance[end] = min(distance[end], distance[start] + weight)

if chk_inf(distance):
    for i in range(2,len(distance)):
        if distance[i] == 1e9:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)