import heapq

def solution(n, s, a, b, fares):
    answer = 0
    INF = 1e9

    dp = [INF for _ in range(n+1)]
    node_dict = {i : [] for i in range(1,n+1)}

    for start, end, weight in fares:
        node_dict[start].append((end, weight))
        node_dict[end].append((start,weight))
    print(node_dict)

    heap = [s]
    dp[s] = 0

    return answer

a = 6
b = 4
c = 6
d = 2
aa = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(a,b,c,d,aa))