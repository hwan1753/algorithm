from sys import stdin


def dfs(start):
    global count
    if matrix[start] == []:
        count += 1
    else:
        for idx in matrix[start]:
            dfs(idx)

count = 0
N = int(stdin.readline())
array_node = list(map(int, stdin.readline().split()))
remove = int(input())



matrix = [[] for _ in range(50)]

for v in range(N):
    if array_node[v] == -1:
        start = v
    else:
        matrix[array_node[v]].append(v)
# print(matrix)

for a in range(N):
    if remove in matrix[a]:
        matrix[a].remove(remove)

if start != remove:
    dfs(start)
print(count)