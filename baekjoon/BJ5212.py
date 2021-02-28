from sys import stdin
import copy

R, C = map(int, stdin.readline().split())

matrix = [list(input()) for _ in range(R)]
result = copy.deepcopy(matrix)

dy = [-1,0,1,0]
dx = [0,-1,0,1]

for y in range(R):
    for x in range(C):
        count = 0
        if matrix[y][x] == '.':
            continue

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C:
                if matrix[ny][nx] == '.':
                    count += 1
            else:
                count += 1
        if count >= 3:
            result[y][x] = '.'

start_y, end_y = 0, 0
for i in range(R):
    if 'X' in result[i]:

        start_y = i
        break
for i in range(R-1, -1,-1):
    if 'X' in result[i]:       
        end_y = i
        break

tmp = []
for j in range(C):
    for i in range(start_y, end_y + 1):
    
        if 'X' == result[i][j]:
            tmp.append(j)
            break


for y in range(start_y, end_y+1):
    print("".join(result[y][tmp[0]:tmp[-1]+1]))
