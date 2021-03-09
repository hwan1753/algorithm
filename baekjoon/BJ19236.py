from sys import stdin

dy = (0,-1,-1,0,1,1,1,0,-1)
dx = (0,0,-1,-1,-1,0,1,1,1)

# [물고기, 방향]
# 물고기 == -1 이면 상어 or 없음
matrix = []

for i in range(4):
    input_ = list(map(int, stdin.readline().split()))
    temp = []
    for j in range(0,8,2):
        temp.append(input_[j:j+2])
    matrix.append(temp)

# 1~16 까지 물고기 찾기
def find_fish():
    for i in range(1,17):
        if i in eat_fish:
            continue
        fish_move(i)

# 찾은 물고기 이동
def fish_move(num):
    for y in range(4):
        for x in range(4):

            if matrix[y][x][0] == num:

                start_d = matrix[y][x][1]
                d = start_d
                while True:
                    
                    my = y + dy[d]
                    mx = x + dx[d]
                    if 0 <= my < 4 and 0 <= mx < 4 and matrix[my][mx][0] != -1:
                        matrix[y][x], matrix[my][mx] = matrix[my][mx], matrix[y][x]
                        return
                    else:
                        if d == 8:
                            d = 1
                        else:
                            d += 1

                        if d == start_d:
                            return


def eating(s_y, s_x):
    d = matrix[s_y][s_x][1]
    temp = []
    my, mx = s_y, s_x
    while True:
        my += dy[d]
        mx += dx[d]
        if 0 <= my < 4 and 0 <= mx < 4:
            if matrix[my][mx] != -1:
                temp.append([my,mx])
        else:
            break
    
    if temp:
        for y, x in temp:
            

        return temp
    else:
        return None


def main(shark_y, shark_x):

    next_ = eating(shark_y, shark_x)
    find_fish()

    while next_:


    
    print()
        

# 처음 1회 실행
shark_y, shark_x = 0, 0
eat_fish = [matrix[0][0][0]]
matrix[0][0][0] = -1

for i in range(1,17):
    if i in eat_fish:
        continue
    chk = fish_move(i)
# 끝까지 재귀로 실행
main()
