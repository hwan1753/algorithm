from _collections import deque

dy = (-2,-2,-1,-1)
dx = (-2,-1,-1,-2)

ddy = (-1,0,1,0)
ddx = (0,1,0,-1)

def solution(maps, p, r):
    answer = 0
    size = len(maps)

    if r == 2:
        for y in range(size):
            for x in range(size):
                count = 0
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]

                    if 0<=ny<y and 0<=nx<x and maps[ny][nx] <= p/2:
                        count += 1
                answer = max(count, answer)

    else:
        for y in range(1, size+1):
            for x in range(1, size+1):
                visit = deque()
                visited = [[0]*size for _ in range(size)]

                count = 0
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    
                    if 0<=ny<size and 0<=nx<size:
                        visit.append((ny,nx))
                        visited[ny][nx] = 1
                        if maps[ny][nx] <= p:
                            count += 1
                # print(y, x, visit, count)
            
                while visit:
                    ny, nx = visit.popleft()

                    for i in range(4):
                        my, mx = ny+ddy[i], nx+ddx[i]

                        if 0<=my<size and 0<=mx<size and visited[my][mx] == 0 and visited[ny][nx]+1 <= r//2:
                            visit.append((my,mx))
                            visited[my][mx] = visited[ny][nx]+1
                            if visited[my][mx] == r//2 and maps[my][mx] <= p/2:
                                count += 1
                            elif visited[my][mx] < r//2 and maps[my][mx] <= p:
                                count += 1
                answer = max(answer, count)
                # print(y,x, count)

    return answer

a = [[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]]	
b = 19
c = 6
print(solution(a,b,c))