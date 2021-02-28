import sys
from collections import deque
T = int(sys.stdin.readline())
for A in range(T):
    n, m = map(int, sys.stdin.readline().split())
    matrix = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    # for aa in matrix:
    #     print(aa)

    queue = deque([1])
    visited = [1]
    answer = 0
    while len(visited) != n:
        value = queue.popleft()
        for idx in range(len(matrix[value])):
            if matrix[value][idx] == 1 and idx not in visited:
                queue.append(idx)
                visited.append(idx)
                answer += 1
        # print(queue)
        # print(visited)
    print(answer)