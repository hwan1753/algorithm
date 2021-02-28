from sys import stdin
from _collections import deque

N, M = map(int, stdin.readline().split())

num_dict = {}

for n in range(1,N+1):
    num_dict[n] = []


taller = [0] * (N+1)    # 큰 횟수
queue = deque([])       # 큐 생성


for _ in range(M):
    A, B = map(int, stdin.readline().split())
    # B에 큰 횟수를 저장
    taller[B] += 1
    # A에서 B로 갈 수 있도록 설정(DFS)
    num_dict[A].append(B)

# 비교에서 큰 적이 없는 값
for num in range(1,N+1):
    if taller[num] == 0:
        queue.append(num)
# 결과값
answer = []

# queue에 값이 있는 동안 반복
while queue:
    now = queue.popleft()
    # 결과값에 추가
    answer.append(str(now))

    # 간선 파악
    for i in num_dict[now]:
        # 1이면 queue에 추가
        if taller[i] == 1:
            queue.append(i)
        taller[i] -= 1
print(" ".join(answer))