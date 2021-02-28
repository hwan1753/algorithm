import heapq


def solution(operations):
    min_heap = []       # 힙 입력 배열
    for i in operations:
        # 숫자 입력인 경우
        if i[0] == "I":
            num = int(i.split()[1])
            # 숫자를 heap에 push
            heapq.heappush(min_heap, num)
        # 최댓값 추출인 경우
        elif i == "D 1":
            # 배열 안에 값이 없으면 패쓰
            if min_heap:
                # nlargest로 가장 최댓값 추출
                min_heap.remove(heapq.nlargest(1, min_heap)[0])
        # 최솟값 추출인 경우
        elif i == "D -1":
            # 배열 안에 값이 없으면 패쓰
            if min_heap:
                # pop으로 최솟값 추출
                heapq.heappop(min_heap)
    # 배열에 값이 있는 경우 최댓값, 최솟값 추출
    # 없는 경우 [0,0]추출
    if min_heap:
        return heapq.nlargest(1, min_heap) + [heapq.heappop(min_heap)]
    return [0, 0]