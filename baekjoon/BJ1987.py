from sys import stdin
from _collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# dfs로 풀 경우 메모이제이션으로 각 알파벳 visit 체크해야함.
def dfs(y, x, ans):
    global answer, chk

    answer = max(ans, answer)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            # print(ny, nx, matrix[ny][nx], chk)
            if matrix[ny][nx] not in chk:
                chk.add(matrix[ny][nx])
                dfs(ny, nx, ans+1)
                chk.remove(matrix[ny][nx])

# bfs로 풀 경우 deque로 할 경우 중복되는 경우 때문에 메모리 초과 발생. set으로 해결해야함.
def bfs(y, x, chk):

    answer = 1
    queue = set([(y, x, chk)])

    while queue:
        ay, ax, chk_val = queue.pop()
        answer = max(answer, len(chk_val))

        for i in range(4):
            ny, nx = ay + dy[i], ax + dx[i]
            if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] not in chk_val:
                queue.add((ny, nx, chk_val + matrix[ny][nx]))
    
    return answer

R, C = map(int, stdin.readline().split())

matrix = [list(map(str, input())) for _ in range(R)]
chk = matrix[0][0]

print(bfs(0,0,chk))