from sys import stdin

node = int(stdin.readline())
m = int(stdin.readline())

edge = {}
for _ in range(m):
    start, end = map(int, stdin.readline().split())
    edge[start] = edge.get(start, []) + [end]
    edge[end] = edge.get(end, []) + [start]

stack = [1]
visited = [0] * (node + 1)
visited[1] = 1

while stack:
    now = stack.pop()
    for i in edge[now]:
        if visited[i] == 1:
            continue
        stack.append(i)
        visited[i] = 1
print(visited.count(1) - 1)