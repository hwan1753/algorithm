from sys import stdin
import heapq


N, E = map(int, stdin.readline().split())
# 노드 해쉬
node_dict = {}
for _ in range(E):
    start, end, weight = map(int, stdin.readline().split())
    # 노드별 해쉬로 저장
    node_dict[start] = node_dict.get(start, []) + [(end, weight)]
    node_dict[end] = node_dict.get(end, []) + [(start, weight)]

# 다익스트라
def dijkstra(start, last):
    # 초기값 설정
    visited = [1e9] * (N + 1)
    # 시작값 0
    visited[start] = 0
    heap = []
    # [거리, 출발점] heap 저장
    heapq.heappush(heap, [0, start])
    
    # 힙에 값이 없을때까지
    while heap:
        _, now = heapq.heappop(heap)
        # 방문 가능한 정점 확인
        for edge in node_dict[now]:
            end, weight = edge[0], edge[1]
            # 만약 값이 이전보다 작은 경우 visited 다시 저장
            if visited[end] > visited[now] + weight:
                visited[end] = visited[now] + weight
                # 힙에도 다시 저장
                heapq.heappush(heap, [visited[end], end])
    return visited[last]

v1, v2 = map(int, stdin.readline().split())
# 만약 간선이 없는 경우 -1 출력
if E == 0:
    print(-1)
else:
    # 정점 v1 먼저 지나는 경우
    answer1 = 0
    answer1 += dijkstra(1,v1)
    if answer1 != -1:
        answer1 += dijkstra(v1,v2)
        if answer1 != -1:
            answer1 += dijkstra(v2,N)
    
    # 정점 v2 먼저 지나는 경우
    answer2 = 0
    answer2 += dijkstra(1,v2)
    if answer2 != -1:
        answer2 += dijkstra(v2,v1)
        if answer2 != -1:
            answer2 += dijkstra(v1,N)

    if answer1 > 1e9 and answer2 > 1e9:
        print(-1)
    else:
        print(min(answer1,answer2))