import heapq

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    min_cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap)+ (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        min_cnt += 1

    return min_cnt

a = [1, 17, 2, 3, 9, 14, 10, 12, 15]
b = 15
solution(a,b)