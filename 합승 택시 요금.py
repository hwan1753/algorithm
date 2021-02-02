import heapq

def dijkstra(node_dict, n, start, end):

    heap = [(0, start)]
    dp = [1e9 for _ in range(n + 1)]
    # dp = [1e9] * (n + 1)
    dp[start] = 0

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for node, w in node_dict[now]:
            if dp[node] > weight + w:
                heapq.heappush(heap, (weight + w, node))
                dp[node] = weight + w
    return dp[end]

def solution(n, s, a, b, fares):

    answer = 1e9

    node_dict = {i:[] for i in range(n+1)}

    for start, end, weight in fares:
        node_dict[start].append((end, weight))
        node_dict[end].append((start,weight))

    for i in range(1,n+1):

        if i == s:
            answer = min(answer, dijkstra(node_dict, n, s, a) + dijkstra(node_dict, n, s, b))
        elif i == a:
            dis_a = dijkstra(node_dict, n, s, a)
            if dis_a < answer:
                answer = min(answer, dis_a + dijkstra(node_dict, n, a, b))

        elif i == b:
            dis_b = dijkstra(node_dict, n, s, b)
            if dis_b < answer:
                answer = min(answer, dis_b + dijkstra(node_dict, n, b, a))
        else:
            dis_i = dijkstra(node_dict, n, s, i)
            if dis_i < answer:
                answer = min(answer, dis_i
                         + dijkstra(node_dict, n, i, a) + dijkstra(node_dict, n, i, b))

    return answer

a = 6
b = 4
c = 6
d = 2
aa = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(a,b,c,d,aa))