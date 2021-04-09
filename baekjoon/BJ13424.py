from sys import stdin
import heapq

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())

    node_dict = {i:[] for i in range(1, N+1)}

    for _ in range(M):
        start, end, weight = map(int, stdin.readline().split())
        node_dict[start] += [(end, weight)]
        node_dict[end] += [(start, weight)]
    K = int(stdin.readline())
    friend = list(map(int,stdin.readline().split()))
    answer = []
    result = 1e9

    for i in range(1, N+1):

        heap = [(0,i)]
        visited = [1e9]*(N+1)
        visited[i] = 0
        
        
        while heap:
            now_weight, start = heapq.heappop(heap)

            if now_weight > visited[start]:
                continue
            
            for end, weight in node_dict[start]:

                if now_weight + weight < visited[end]:
                    visited[end] = now_weight + weight
                    heapq.heappush(heap, (now_weight+weight, end))
            
        temp = [visited[j] for j in friend]
        
        if sum(temp) < result:
            result = sum(temp)
            answer = [i]
        elif sum(temp) == result:
            answer.append(i)
    print(min(answer))