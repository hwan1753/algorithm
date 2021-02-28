from sys import stdin
import heapq
from itertools import chain

# 상하좌우
dy = [-1,0,1,0]
dx = [0,-1,0,1]

# n 개 매트릭스
n = int(stdin.readline())
# 매트릭스 값 입력
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
# 메모이제이션
memoization = [[0] * n for _ in range(n)]
# 최대 힙정렬 할 배열
heap = []

# 최대 힙 정렬
for y in range(n):
    for x in range(n):
        # heapq는 최소힙정렬이므로 -1을 곱해서 최대힙정렬로 한다.
        heapq.heappush(heap, (-1 * matrix[y][x], y, x))


# heap에 값이 없을때까지
while heap:
    _, y, x = heapq.heappop(heap)
    chk_arr = []
    # 상하좌우 체크
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            # 만약 상,하,좌,우 값이 더 크다면 해당 메모값 배열에 추가
            if matrix[y][x] < matrix[ny][nx]:
                chk_arr.append(memoization[ny][nx])

    if chk_arr: # 만약 배열에 값이 있으면 가장 큰 값 + 1
        memoization[y][x] = max(chk_arr) + 1
    else: # 배열에 값이 없으면 1
        memoization[y][x] = 1
# 메모 중에서 가장 큰 값 출력
print(max(chain(*memoization)))