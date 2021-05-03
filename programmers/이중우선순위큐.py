import heapq

def solution(operations):
    answer = []
    heap = []

    for i in operations:
        temp = i.split()
        if temp[0] == "I":
            heapq.heappush(heap, int(temp[1]))
        elif heap and temp[0] == "D" and temp[1] == "-1":
            heapq.heappop(heap)
        elif heap and temp[0] == "D" and temp[1] == "1":
            heap.remove(heapq.nlargest(1,heap)[0])
    
    if heap:
        answer.append(heapq.nlargest(1,heap)[0])
        answer.append(heapq.heappop(heap))
    else:
        answer = [0,0]

    return answer

a = ["I 16","D 1"]	
print(solution(a))