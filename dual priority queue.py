import heapq


def solution(operations):
    answer = []
    # max_heap = []
    min_heap = []
    for i in operations:
        if i[0] == "I":
            num = int(i.split()[1])
            # heapq.heappush(max_heap, -1 * num)
            heapq.heappush(min_heap, num)
        elif i == "D 1":
            if min_heap:
                min_heap.remove(heapq.nlargest(1, min_heap)[0])

            # print(heapq.nlargest(1,min_heap), "!!!")
        elif i == "D -1":
            if min_heap:
                heapq.heappop(min_heap)
        # print(max_heap)
        # print(min_heap)
        # print("_"*10)
    if min_heap:
        return heapq.nlargest(1, min_heap) + [heapq.heappop(min_heap)]
    return [0, 0]

import math

print(math.gcd(4,6))