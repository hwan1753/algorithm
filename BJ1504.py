from sys import stdin
import heapq


N, E = map(int, stdin.readline().split())
node_dict = {}
for _ in range(E):
    start, end, weight = map(int, stdin.readline().split())
    node_dict[start] = node_dict.get(start, []) + [(end, weight)]
    node_dict[end] = node_dict.get(end, []) + [(start, weight)]

def dijkstra(start, last):
    visited = [1e9] * (N + 1)
    visited[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        _, now = heapq.heappop(heap)
        # if now == last:
        #     answer += visited[now]
        #     return answer

        for edge in node_dict[now]:
            end, weight = edge[0], edge[1]
            # if last == N:
            #     if visited[end] > visited[now] + weight:
            #         visited[end] = visited[now] + weight
            #         heapq.heappush(heap, [visited[end], end])
            # else:
            #     if end == N:
            #         continue
            if visited[end] > visited[now] + weight:
                visited[end] = visited[now] + weight
                heapq.heappush(heap, [visited[end], end])
    return visited[last]
    # return -1

v1, v2 = map(int, stdin.readline().split())
if E == 0:
    print(-1)
else:
    answer1 = 0
    answer1 += dijkstra(1,v1)
    if answer1 != -1:
        answer1 += dijkstra(v1,v2)
        if answer1 != -1:
            answer1 += dijkstra(v2,N)

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

# heapq.heappush(heap, [0, 1])
# chk_v1, chk_v2 = False, False
#
#
#
# heap = []
# visited = [9999999] * (N+1)
# if chk_v1:
#     visited[v1] = 0
#     heapq.heappush(heap, [0, v1])
# elif chk_v2:
#     visited[v2] = 0
#     heapq.heappush(heap, [0, v2])
#
#
#
# while heap:
#     _, now = heapq.heappop(heap)
#     if now == v1:
#         chk_v1 = True
#
#     elif now == v2:
#         chk_v2 = True
#
#     if chk_v1 and chk_v2:
#         answer += visited[now]
#         break
#
#     for edge in node_dict[now]:
#         end, weight = edge[0], edge[1]
#         if end == N:
#             continue
#         if visited[end] > visited[now] + weight:
#             visited[end] = visited[now] + weight
#             heapq.heappush(heap, [visited[end], end])
#
# heap = []
# visited = [9999999] * (N+1)
# if chk_v1 and chk_v2:
#     visited[now] = 0
#     heapq.heappush(heap, [0,now])
# chk_final = True
#
# while heap:
#     _, now = heapq.heappop(heap)
#     if now == N:
#         chk_final = False
#         print(visited[now] + answer)
#         break
#
#     for edge in node_dict[now]:
#         end, weight = edge[0], edge[1]
#         if visited[end] > visited[now] + weight:
#             visited[end] = visited[now] + weight
#             heapq.heappush(heap, [visited[end], end])
# if chk_final:
#     print(-1)