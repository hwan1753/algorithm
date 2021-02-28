from sys import stdin
from _collections import deque

N, K = map(int,stdin.readline().split())


visited = [0] * 100001

queue = deque()

visited[N] = 1
queue.append(N)

walk = [-1,1]
jump = 2

while queue:
    if visited[K] != 0:
        break
    loc = queue.popleft()
    for y in walk:
        if 0 <= loc + y < 100001:
            if visited[loc + y] == 0:
                queue.append(loc + y)
                visited[loc + y] = visited[loc] + 1
    if 0 <= loc * jump < 100001:
        if visited[loc * jump] == 0:
            queue.append(loc*jump)
            visited[loc*jump] = visited[loc] + 1
    # print(queue)
print(visited[K] - 1)