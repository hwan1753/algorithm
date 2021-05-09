from pprint import pprint

def solution(places):

    # 상하좌우
    dy = (-1,0,1,0)
    dx = (0,1,0,-1)

    # 대각
    ddy = (-1,-1,1,1)
    ddx = (-1,1,1,-1)

    # 상하좌우 거리 2
    dddy = (-2,0,2,0)
    dddx = (0,2,0,-2)

    answer = []
    
    for case in places:
        board = []
        for c in case:
            board.append(list(map(str, c)))
        correct = True

        for y in range(5):
            if not correct: break
            for x in range(5):
                if not correct: break
                if board[y][x] != 'P':
                    continue

                for n in range(4):
                    ny, nx = y+dy[n], x+dx[n]
                    cy, cx = y+dddy[n], x+dddx[n]
                    if 0<=ny<5 and 0<=nx<5:
                        if board[ny][nx] == 'P':
                            correct = False
                            break
                        elif 0<=cy<5 and 0<=cx<5 and board[ny][nx] == 'O' and board[cy][cx] == 'P':
                            correct = False
                            break
                    
                for n in range(4):
                    nny, nnx = y+ddy[n], x+ddx[n]
                    cy1, cx1 = y+dy[n], x+dx[n]
                    cy2, cx2 = y+dy[n-1], x+dx[n-1]

                    if 0<=nny<5 and 0<=nnx<5 and board[nny][nnx] == 'P':
                        if 0<=cy1<5 and 0<=cx1<5 and board[cy1][cx1] != 'X':
                            correct = False
                            break
                        if 0<=cy2<5 and 0<=cx2<5 and board[cy2][cx2] != 'X':
                            correct = False
                            break
        
        if correct:
            answer.append(1)
        else:
            answer.append(0)

    return answer

a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	
print(solution(a))