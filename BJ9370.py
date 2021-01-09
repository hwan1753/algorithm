from sys import stdin
import heapq

# 방문여부 확인용 초기값
INF = 1e9

# 다익스트라 알고리즘
def dijkstra(start, last):
    # 방문여부
    dp = [INF] * (n+1)
    # 시작 값 0부터 시작
    dp[start] = 0
    heap = []
    # 힙에 (거리값, 정점) push, 우선순위 큐
    heapq.heappush(heap, (dp[start], start))

    # 힙이 있을때까지
    while heap:
        
        weight, now = heapq.heappop(heap)
        for end, dis in node_dict[now]:
            # 조건을 만족하는 값 heap정렬
            if dp[end] > weight + dis:
                dp[end] = weight + dis
                heapq.heappush(heap, (dp[end], end))
    return dp[last]


T = int(stdin.readline())
for _ in range(T):
    n, m, t = map(int, stdin.readline().split())
    s, g, h = map(int, stdin.readline().split())


    # 노드 hash화
    node_dict = {}

    for _ in range(m):
        a, b, d = map(int, stdin.readline().split())
        node_dict[a] = node_dict.get(a,[]) + [(b,d)]
        node_dict[b] = node_dict.get(b, []) + [(a, d)]
    
    # 1번 시작 -> g -> h -> 최종
    # 2번 시작 -> h -> g -> 최종
    answer1, answer2 = 0, 0

    answer1 = dijkstra(s, g) + dijkstra(g, h)
    answer2 = dijkstra(s, h) + dijkstra(h, g)

    candidate = []
    minimum = INF
    for _ in range(t):
        node = int(stdin.readline())
        answer = min(answer1 + dijkstra(h, node), answer2 + dijkstra(g, node))
        chk_answer = dijkstra(s, node)

        if chk_answer >= answer:
            heapq.heappush(candidate, node)


    while candidate:
        print(heapq.heappop(candidate), end="")
        if candidate:
            print(" ", end="")
        else:
            print("")