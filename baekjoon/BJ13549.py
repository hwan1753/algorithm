from _collections import deque

N, K = map(int, input().split())

visited = [1e9] * 100001

visited[N] = 0
visit = deque()
visit.append(N)

while visit and visit[0] != K:
    loc = visit.popleft()
    

    if loc+ 1 < 100001 and visited[loc+1] > visited[loc] + 1:
        visit.append(loc+1)
        visited[loc+1] = visited[loc] + 1

    if loc-1 >= 0 and visited[loc-1] > visited[loc]+1:
        visit.append(loc-1)
        visited[loc-1] = visited[loc] + 1

    if loc*2 < 100001 and visited[loc*2] > visited[loc]:
        visit.append(loc*2)
        visited[loc*2] = visited[loc]

print(visited[K])