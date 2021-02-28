from sys import stdin
from _collections import deque

Test = int(stdin.readline())
for case in range(Test):
    N, M = map(int,stdin.readline().split())
    doc = list(map(int, stdin.readline().split()))
    arr = []

    for idx in range(N):
        arr.append([doc[idx], idx])
    queue = deque(arr)

    answer = 0
    while True:
        chk = queue.popleft()
        if not queue:
            answer += 1
            print(answer)
            break

        if chk[0] >= max(queue)[0] and chk[1] == M:
            answer += 1
            print(answer)
            break
        elif chk[0] >= max(queue)[0]:
            answer += 1
        else:
            queue.append(chk)

