import heapq
from collections import deque

def solution(jobs):
    schedule = deque([])
    working = 0
    answer = 0
    heap = []
    tmp = []
    idx = 0

    while idx < len(jobs):
        if len(schedule) == 0:
            for time in range(jobs[idx][1]-jobs[idx][0]):
                schedule.append(1)

        else:
            if jobs[idx][0] < len(schedule):
                tmp.append(jobs[idx])
        #     else:
        #         time = schedule.popleft()
        #         answer += (time[1] - time[0])
        #         idx = 0
        #         while len(schedule) != 0:
        #             out = schedule.popleft()
        #             chk = answer + out[1] - out[0]
        #             tmp.append(chk)
        idx += 1
    print(schedule)
    print(tmp)
    return answer

a = [[0, 3], [1, 9], [2, 6]]

solution(a)