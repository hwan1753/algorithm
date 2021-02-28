import heapq
from collections import deque

def solution(jobs):

    schedule = deque(sorted(jobs))
    jobs_done = len(jobs)
    current_time = 0
    working = 0
    answer = 0
    tmp = []
    idx = 0

    while idx < jobs_done:
        if not tmp:
            start, working = schedule.popleft()
            current_time = start + working
            answer += working
        else:

            working, time = heapq.heappop(tmp)
            current_time += working
            answer += current_time - time
        # print(answer)
        idx += 1

        while schedule and schedule[0][0] <= current_time:
            heapq.heappush(tmp, schedule.popleft()[::-1])
        # print(tmp)

    return answer // jobs_done

a = [[0, 3], [1, 9], [2, 6]]
# aa = deque(a[::-1])
# print(aa.popleft())
print(solution(a))