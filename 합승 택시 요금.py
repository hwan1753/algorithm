import heapq

# 다익스트라
def dijkstra(node_dict, n, start, end):
    # 우선순위 queue 활용.
    heap = [(0, start)]
    # 거리 저장.
    dp = [1e9 for _ in range(n + 1)]
    dp[start] = 0

    # heap이 있을때
    while heap:
        # 우선순위가 높은 것 먼저 처리
        weight, now = heapq.heappop(heap)
        # 만약 이미 저장된 거리가 더 작은 경우 패스
        if dp[now] < weight:
            continue
        # 해당 노드에서 이어지는 간선확인
        for node, w in node_dict[now]:
            # 만약 지금 거리 + 다음 거리가 저장된 거리보다 작은 경우
            if dp[node] > weight + w:
                heapq.heappush(heap, (weight + w, node))
                dp[node] = weight + w
    return dp[end]

def solution(n, s, a, b, fares):

    answer = 1e9
    # 모든 노드 hash화
    node_dict = {i:[] for i in range(n+1)}
    # matrix를 hash로 변환
    for start, end, weight in fares:
        node_dict[start].append((end, weight))
        node_dict[end].append((start,weight))

    # 같이 택시타는 곳(모든 곳을 탐색)
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