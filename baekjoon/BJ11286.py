from sys import stdin
import heapq

N = int(stdin.readline())
# 우선순위 큐
heap = []

for n in range(N):
    num = int(stdin.readline())
    if num != 0:
        # 0이 아닌 경우 우선순위 큐에 (절대값, 숫자) 삽입
        heapq.heappush(heap,(abs(num), num))
    # 0인경우
    else:
        # 큐가 비어있으면 0 출력
        if len(heap) == 0:
            print(0)
        else:
            # 큐에 값이 있으면 pop
            print(heapq.heappop(heap)[1])