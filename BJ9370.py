from sys import stdin
import heapq

INF = 1e9

def dijkstra(start, last):
    dp = [INF] * (n+1)
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (dp[start], start))

    while heap:
        weight, now = heapq.heappop(heap)
        for end, dis in node_dict[now]:
            if dp[end] > weight + dis:
                dp[end] = weight + dis
                heapq.heappush(heap, (dp[end], end))
    return dp[last]


T = int(stdin.readline())
for _ in range(T):
    n, m, t = map(int, stdin.readline().split())
    s, g, h = map(int, stdin.readline().split())


    node_dict = {}

    for _ in range(m):
        a, b, d = map(int, stdin.readline().split())
        node_dict[a] = node_dict.get(a,[]) + [(b,d)]
        node_dict[b] = node_dict.get(b, []) + [(a, d)]

    answer1, answer2 = 0, 0

    answer1 = dijkstra(s, g) + dijkstra(g, h)
    answer2 = dijkstra(s, h) + dijkstra(h, g)

    candidate = []
    minimum = INF
    for _ in range(t):
        node = int(stdin.readline())
        # print("!!")
        # answer1 += dijkstra(h, node)
        # answer2 += dijkstra(g, node)
        answer = min(answer1 + dijkstra(h, node), answer2 + dijkstra(g, node))
        chk_answer = dijkstra(s, node)

        # print(answer1 + dijkstra(h, node), answer2 + dijkstra(g, node))
        if chk_answer >= answer:
            heapq.heappush(candidate, node)


    while candidate:
        print(heapq.heappop(candidate), end="")
        if candidate:
            print(" ", end="")
        else:
            print("")