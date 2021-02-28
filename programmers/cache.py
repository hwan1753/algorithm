from _collections import deque

def solution(cacheSize, cities):
    queue = deque([0] * cacheSize)  # 캐시 생성
    answer = 0     # 정답값
    if cacheSize == 0:  # 캐시가 0이면 전부 chache miss
        return 5 * len(cities)
    for name in cities:     # 캐시 메모리에 돌리기
        name = name.lower() # 전부 소문자로
        if name in queue:   # 만약 도시가 캐시에 있다면
            queue.remove(name)  # 캐시 최신으로 교체
            queue.append(name)
            answer += 1     # cache hit

        else:
            queue.popleft() # 가장 옛날 캐시 삭제
            queue.append(name)  # 캐시에 추가
            answer += 5     # cache miss

    return answer   # 정답 리턴
a = 3
b = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
c = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

print(solution(a,b))