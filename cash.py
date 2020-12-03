from _collections import deque

def solution(cacheSize, cities):
    queue = deque([0] * cacheSize)
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    for name in cities:
        name = name.lower()
        if name in queue:
            queue.remove(name)
            queue.append(name)
            answer += 1

        else:
            queue.popleft()
            queue.append(name)
            answer += 5

    return answer
a = 3
b = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
c = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

print(solution(a,b))
# print(solution(a,c))