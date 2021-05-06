# Floyd
BIGBIG = 1e9
def solution(V, edge):
    graph = [[BIGBIG] * V for a in range(V)]
    matched = [[False] * V for a in range(V)]
    for a in range(V):
        graph[a][a] = 0

    for a,b in edge:
        a,b = a-1, b-1
        graph[a][b] = 1
        matched[a][b] = matched[b][a] = True

    for k in range(V):
        for a in range(V):
            for b in range(V):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(V):
        for b in range(V):
            if graph[a][b] != BIGBIG:
                matched[a][b] = matched[b][a] = True

    return sum(all(a) for a in matched)

a = 5
b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(a,b))