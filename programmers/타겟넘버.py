from _collections import deque

def solution(numbers, target):
    cnt = 0
    idx = 0
    def operator(idx):
        if idx < len(numbers):
            operator(idx + 1)

            numbers[idx] *= -1
            operator(idx + 1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1
    operator(idx)
    return cnt

from collections import deque

def solution2(numbers, target):
    graph = []
    inque = deque()

    graph.append([numbers[0],numbers[0]*-1])
    inque.append([numbers[0],0])
    inque.append([numbers[0]*-1, 1])
    for order in range(1,len(numbers)):
        graph.append([])
        count = len(inque)
        
        for num in range(0,2 * count,2):
            value = inque.popleft()
            graph[order].append(value[0] + numbers[order])
            graph[order].append(value[0] - numbers[order])
            inque.append([value[0] + numbers[order],num])
            inque.append([value[0] - numbers[order], num+1])
    result = 0
    for a in graph[len(numbers)-1]:
        if a == target:
            result += 1

    return result
a = [1, 1, 1, 1, 1]
b = 3
print(solution2(a,b))