import random
import heapq

# 힙을 활용한 탐색
def solution(a):
    answer = 0
    min_idx = a.index(min(a))
    answer += 1
    heap_left, heap_right = [], []
    
    if min_idx == 0:
        for i in range(min_idx+1, len(a)):
            heap_right.append((a[i],i))
        # heap_right = a[min_idx+1:].copy()
    elif min_idx == len(a) - 1:
        # heap_left = a[:min_idx].copy()
        for j in range(min_idx):
            heap_left.append((a[j],j))
    else:
        # heap_left, heap_right = a[:min_idx].copy(), a[min_idx+1:].copy()
        for i in range(min_idx+1, len(a)):
            heap_right.append((a[i],i))
        for j in range(min_idx):
            heap_left.append((a[j],j))


    heapq.heapify(heap_left)
    heapq.heapify(heap_right)
    temp  = 1000000

    while heap_left:
        chk_lmin = heapq.heappop(heap_left)
        chk_idx = chk_lmin[1]
        if chk_idx == 0:
            answer += 1
            break
        elif chk_idx < temp:
            answer += 1
            temp = chk_idx

    temp2 = 0
    while heap_right:
        chk_rmin = heapq.heappop(heap_right)
        chk_idx = chk_rmin[1]
        if chk_idx == len(a) - 1:
            answer += 1
            break
        elif chk_idx > temp2:
            temp2 = chk_idx
            answer += 1
    return answer

# 단순 계산 알고리즘(완전탐색)
def solution2(a):
    answer = 0

    minimum = min(a)
    min_idx = a.index(minimum)
    answer += 1
    min_lidx, min_ridx = 0, len(a) - 1

    if min_idx == 0:
        min_ridx = a.index(min(a[min_idx+1:]))
        answer += 1
    elif min_idx == len(a) - 1:
        min_lidx = a.index(min(a[:min_idx]))
        answer += 1
    else:
        min_ridx = a.index(min(a[min_idx + 1:]))
        min_lidx = a.index(min(a[:min_idx]))
        answer += 2

    while min_lidx > 0:
        min_lidx = a.index(min(a[:min_lidx]))
        answer += 1

    while min_ridx < len(a) - 1:
        min_ridx = a.index(min(a[min_ridx+1:]))
        answer += 1

    return answer

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
b = [9, -1, -5]
c = [9, -1, -5, -2, -3]
d = random.sample(range(-1000000,1000000),100)
# print(len(d))
print(solution(d))
print(solution2(d))