from sys import stdin
from _collections import defaultdict, deque

N, L, R = map(int, stdin.readline().split())

board = [list(map(int, stdin.readline().split())) for _ in range(N)]

dy = (1,0)
dx = (0,1)


def chk_link():

    link = defaultdict(list)
    
    for y in range(N):
        for x in range(N):
            for d in range(2):
                
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < N and L <= abs(board[y][x] - board[ny][nx]) <= R:
                    link[(y,x)] += [(ny,nx)]
                    link[(ny,nx)] += [(y,x)]
    if link:
        return link
    return None


def move_people(link):

    arr = []
    visited = [[0]*N for _ in range(N)]
    visit = deque()

    for y, x in link.keys():

        chk_ = []    
        if visited[y][x] == 1:
            continue
        
        visited[y][x] = 1
        visit.append((y,x))
        chk_.append((y,x))

        while visit:
            temp = visit.popleft()
            
            for ny, nx in link[temp]:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    visit.append((ny,nx))
                    chk_.append((ny,nx))
            
        arr.append(chk_)
    
    return arr


def calcul(arr):
    global board

    for i in arr:
        sum_ = 0
        for y, x in i:
            sum_ += board[y][x]

        for y, x in i:
            board[y][x] = int(sum_ / len(i))


def main():
    
    answer = 0
    while True:
        link = chk_link()
        if link:
            arr = move_people(link)
            calcul(arr)
            answer += 1
        else:
            break
    print(answer)


main()