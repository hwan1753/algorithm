import random
import heapq

# 힙을 활용한 탐색
def solution(a):

    answer = 0      # 결과값
    min_idx = a.index(min(a))   # 가장 작은 숫자의 인덱스
    answer += 1
    heap_left, heap_right = [], []  # min_idx를 기준으로 왼쪽, 오른쪽

    # 만약 min_idx의 왼쪽이 없을 경우
    if min_idx == 0:
        for i in range(min_idx+1, len(a)):
            heap_right.append((a[i],i))
    # 만약 min_idx의 오른쪽이 없을 경우
    elif min_idx == len(a) - 1:
        for j in range(min_idx):
            heap_left.append((a[j],j))
    # min_idx의 왼쪽, 오른쪽
    else:
        for i in range(min_idx+1, len(a)):
            heap_right.append((a[i],i))
        for j in range(min_idx):
            heap_left.append((a[j],j))

    # 왼쪽, 오른쪽 heap정렬
    heapq.heapify(heap_left)
    heapq.heapify(heap_right)

    temp  = 1000000     # 확인용 변수
    while heap_left:
        chk_lmin = heapq.heappop(heap_left)
        chk_idx = chk_lmin[1]
        # 가장 작은 값 인덱스가 0인 경우
        if chk_idx == 0:
            answer += 1
            break
        # heap에서 가장 작은 값은 이전 값보다 왼쪽에 있어야함.
        elif chk_idx < temp:
            answer += 1
            temp = chk_idx

    temp2 = 0   # 확인용 변수
    while heap_right:
        chk_rmin = heapq.heappop(heap_right)
        chk_idx = chk_rmin[1]
        # 가장 작은 값 인덱스가 마지막인 경우
        if chk_idx == len(a) - 1:
            answer += 1
            break
        # heap에서 가장 작은 값은 이전 값보다 오른쪽에 있어야 함.
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