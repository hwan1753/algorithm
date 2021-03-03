from sys import stdin
from _collections import deque

N, M = map(int,stdin.readline().split())

ladder = dict(map(int, stdin.readline().split()) for _ in range(N))
snake = dict(map(int, stdin.readline().split()) for _ in range(M))

visited = [1e9] * 101
visit = deque([1])
visited[1] = 0

while visit:
    loc = visit.popleft()
    

    for i in range(6,0,-1):
        if loc + i < 101 and visited[loc + i] > visited[loc] + 1:
            
            if loc + i in ladder:
                if visited[ladder[loc + i]] > visited[loc] + 1:
                    visit.append(ladder[loc+i])
                    visited[ladder[loc+i]] = visited[loc] + 1
                    visited[loc+i] = visited[loc] + 1
            elif loc + i in snake:
                if visited[snake[loc + i]] > visited[loc] + 1:
                    visit.append(snake[loc+i])
                    visited[snake[loc+i]] = visited[loc] + 1
                    visited[loc+i] = visited[loc] + 1
            else:
                visit.append(loc + i)
                visited[loc + i] = visited[loc] + 1

    if 100 in visit:
        print(visited[100])
        break