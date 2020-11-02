from collections import deque
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2



def solution(scoville, K):
    array = sorted(scoville)
    result = 0
    chk = 0
    while chk < K:
        fir, sec = array[0], array[1]
        del array[0]
        del array[0]
        chk = fir + sec * 2

        print(chk)
        array.append(chk)
        st = len(array)-1
        while True:
            if chk < array[st//2]:
                array[st] = array[st//2]
                array[st//2] = chk
                st = st // 2
                print(array)
            else:
                break
        print(array)
        result += 1

    return result

a = [1, 17, 2, 3, 9, 14, 10, 12, 15]
b = 15
solution(a,b)