from _collections import deque

def solution(n, vertex):
    answer = 0

    node_dict = {i:[] for i in range(1,n+1)}

    for i, j in vertex:
        node_dict[i].append(j)
        node_dict[j].append(i)
    
    visit = deque()
    visited = [0]*(n+1)

    visit.append(1)
    visited[1] = 1

    while visit:
        loc = visit.popleft()

        for i in node_dict[loc]:
            if visited[i] == 0:
                visit.append(i)
                visited[i] = visited[loc]+1

    return visited.count(max(visited))

a = 6
a2 = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(a,a2))