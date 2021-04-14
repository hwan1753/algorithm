from sys import stdin
import heapq

N, M = map(int, stdin.readline().split())

node_dict = {i:[] for i in range(1,N+1)}
heap = []
for _ in range(M):
    start, end, weight = map(int, stdin.readline().split())
    node_dict[start] += [[end, weight]]
    node_dict[end] += [[start, weight]]

    heapq.heappush(heap,(weight, start, end))


chk_arr = [i for i in range(N+1)]
answer = 0
count = 0
# print('-'*10)
while heap:
    weight, loc_a, loc_b = heapq.heappop(heap)
    if chk_arr[loc_a] != chk_arr[loc_b]:
        answer += weight
        count += 1
        arr = [loc_b]
        # print(loc_a, loc_b, weight)
        for j in range(1, N+1):
            if chk_arr[j] == chk_arr[loc_b]:
                arr.append(j)

        for i in arr:    
            chk_arr[i] = chk_arr[loc_a]
        
        if count == N+1:
            break

print(answer - weight)