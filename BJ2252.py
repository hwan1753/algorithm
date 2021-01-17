from sys import stdin
from _collections import deque

N, M = map(int, stdin.readline().split())

num_dict = {}

for n in range(1,N+1):
    num_dict[n] = []


taller = [0] * (N+1)
queue = deque([])

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    taller[B] += 1
    num_dict[A].append(B)

for num in range(1,N+1):
    if taller[num] == 0:
        queue.append(num)

answer = []

while queue:
    now = queue.popleft()
    answer.append(str(now))

    for i in num_dict[now]:
        if taller[i] == 1:
            queue.append(i)
        taller[i] -= 1
print(" ".join(answer))