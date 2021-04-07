from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
node_dict = {i:[] for i in range(1,n+1)}
for _ in range(m):
    A, B = map(int, stdin.readline().split())
    node_dict[A] += [B]

visited = [1e9] * (n+1)
visit = deque([x])
visited[x] = 0

while visit:
    loc = visit.popleft()

    for i in node_dict[loc]:
        if visited[i] > visited[loc] + 1:
            visited[i] = visited[loc] + 1
            visit.append(i)

res = visited.count(k)

if res == 0:
    print(-1)
else:
    for i in range(1,n+1):
        if visited[i] == k:
            print(i)