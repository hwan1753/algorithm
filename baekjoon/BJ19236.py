from sys import stdin
from copy import deepcopy

dy = (0,-1,-1,0,1,1,1,0,-1)
dx = (0,0,-1,-1,-1,0,1,1,1)

# [물고기, 방향]
# 물고기 == -1 이면 상어 or 없음
origin_matrix = []

for i in range(4):
    input_ = list(map(int, stdin.readline().split()))
    temp = []
    for j in range(0,8,2):
        temp.append(input_[j:j+2])
    origin_matrix.append(temp)

# 1~16 까지 물고기 찾기
def find_fish(matrix, eat_fish):
    for i in range(1,17):
        if i in eat_fish:
            continue
        
        fish_move(i, matrix)
    
        # for a in matrix:
        #     print(a)
        # print("="*20)

# 찾은 물고기 이동
def fish_move(num, matrix):
    for y in range(4):
        for x in range(4):

            if matrix[y][x][0] == num:

                start_d = matrix[y][x][1]
                d = start_d
                while True:
                    
                    my = y + dy[d]
                    mx = x + dx[d]
                    if 0 <= my < 4 and 0 <= mx < 4 and matrix[my][mx][0] != -1:
                        matrix[y][x][1] = d
                        matrix[y][x], matrix[my][mx] = matrix[my][mx], matrix[y][x]
                        return 
                    else:
                        if d == 8:
                            d = 1
                        else:
                            d += 1

                        if d == start_d:
                            return


def eating(s_y, s_x, matrix):
    d = matrix[s_y][s_x][1]
    candidate = []
    my, mx = s_y, s_x
    while True:
        my += dy[d]
        mx += dx[d]
        if 0 <= my < 4 and 0 <= mx < 4:
            if matrix[my][mx][0] > 0:
                candidate.append([my,mx])
        else:
            break
    
    if candidate:
        return candidate
    else:
        return None


def main(shark_y, shark_x, eat_fish, matrix):


    answer = 0      # 최대 값 찾는 변수
    temp_matrix = deepcopy(matrix)  # matrix 복사.
    temp_matrix[shark_y][shark_x][0] = -1   # 상어 위치 표시

    find_fish(temp_matrix, eat_fish)    # 물고기 이동
    next_ = eating(shark_y, shark_x, temp_matrix)   # 다음 상어가능 위치
    
    # 다음 상어 있는 경우
    # 상어 위치별로 재귀(벡트래킹)
    if next_:
        # 이전 상어위치 빈칸으로 변경
        temp_matrix[shark_y][shark_x][0] = 0
        # 가능한 상어위치로 이동
        for next_y, next_x in next_:
            next_fish = temp_matrix[next_y][next_x][0]
            # 가장 값이 높은 값으로 반영
            answer = max(answer, main(next_y, next_x, eat_fish +[next_fish], temp_matrix))
        return answer
    
    # 없는 경우 먹은 물고기 값 return
    else:
        return sum(eat_fish)

        

# 최초 상어 위치
shark_y, shark_x = 0, 0

print(main(shark_y, shark_x, [origin_matrix[shark_y][shark_x][0]], origin_matrix))
