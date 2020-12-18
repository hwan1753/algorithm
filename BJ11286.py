from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for n in range(N):
    num = int(stdin.readline())
    if num != 0:
        heapq.heappush(heap,(abs(num), num))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])