from sys import stdin
from itertools import chain

def dfs(arr, num, visited):

    for line in arr_line:
        if line[0] == num:
            if line[1] not in visited:
                visited.append(line[1])
                visited = dfs(arr, line[1], visited)
        elif line[1] == num:
            if line[0] not in visited:
                visited.append(line[0])
                visited = dfs(arr, line[0], visited)

    return visited

N, M = map(int, stdin.readline().split())
arr_line = []
for i in range(M):
    arr_line.append(list(map(int,stdin.readline().split())))

answer = 0
visited = []

for po in range(1,N+1):
    if po not in visited:
        if po in list(chain(*arr_line)):
            visited.append(po)
            visited = dfs(arr_line, po, visited)
            # print(visited)
            answer += 1
            # print(po)
        else:
            visited.append(po)
            answer += 1
print(answer)