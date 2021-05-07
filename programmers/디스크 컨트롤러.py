import heapq
from copy import deepcopy

def solution(jobs):
    answer = 0
    jobs.sort()
    heap_start = deepcopy(jobs)
    heapq.heapify(heap_start)
    now, doing = heapq.heappop(heap_start)

    answer += doing
    time = now + doing
    ready = []

    while heap_start or ready:
        
        while heap_start and heap_start[0][0] <= time:
            start, doing = heapq.heappop(heap_start)
            heapq.heappush(ready, (doing, time))
            answer += time - start

        if ready:
            doing, _ = heapq.heappop(ready)
            time += doing
            answer += doing * (len(ready)+1)
        elif heap_start:
            time, doing = heapq.heappop(heap_start)
            time += doing
            answer += doing
            
    return (answer // len(jobs))

a = [[0, 3], [1, 9], [2, 6]]	
print(solution(a))