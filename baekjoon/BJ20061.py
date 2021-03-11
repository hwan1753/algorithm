from sys import stdin
from _collections import deque

N = int(stdin.readline())


input_block = deque([list(map(int, stdin.readline().split())) for _ in range(N)])

green_matrix = [[0]*4 for _ in range(6)]
blue_matrix = [[0]*6 for _ in range(4)]
score = 0

def input_green(t, x, y,green_matrix):

    for i in range(5,-1,-1):

        if t == 2:
            if green_matrix[i][y] == 0 and green_matrix[i][y+1] == 0:
                green_matrix[i][y], green_matrix[i][y+1] = 1, 1
                return
        
        elif t == 3:
            if i+1 < 6 and green_matrix[i][y] == 0 and green_matrix[i+1][y] == 0:
                green_matrix[i][y], green_matrix[i+1][y] = 1, 1
                return

        else:
            if green_matrix[i][y] == 0:
                green_matrix[i][y] = 1
                return

def input_blue(t,x,y,blue_matrix):
    
    for i in range(5,-1,-1):

        if t == 2:
            if i+1 < 5 and blue_matrix[x][i] == 0 and blue_matrix[x][i+1] == 0:
                blue_matrix[x][i], blue_matrix[x][i+1] = 1, 1
                return
        
        elif t == 3:
            if blue_matrix[x][i] == 0 and blue_matrix[x+1][i] == 0:
                blue_matrix[x][i], blue_matrix[x+1][i] = 1, 1
                return

        else:
            if blue_matrix[x][i] == 0:
                blue_matrix[x][i] = 1
                return

def chk_score_green(score,green_matrix):
    idx = 5
    while idx > 1: 
        if 0 not in green_matrix[idx]:
            score += 1
            green_matrix = [[0]*4] + green_matrix[:idx] + green_matrix[idx+1:]
        
        else:
            idx -= 1
    return score, green_matrix

def chk_score_blue(score,blue_matrix):
    idx = 5
    while idx > 1:
        for i in range(4):
            chk = 0
            if blue_matrix[i][idx] == 1:
                chk += 1
            else:
                break
        if chk == 4:
            scrore += 1
            for i in range(4):
                blue_matrix[i] = [0] + blue_matrix[i][:idx] + blue_matrix[i][idx+1:]
        else:
            idx -= 1
    return score, blue_matrix



def chk_special_green():
    idx = 1
    while idx > -1:
        if 1 in green_matrix[idx]:
            green_matrix = [[0]*4] + green_matrix[:-1]
        else:
            idx -= 1


def chk_special_blue():
    idx = 1
    while idx > -1:
        for i in range(4):
    

def main(green_matrix, blue_matrix):
    score = 0
    while input_block:
        
        t, x, y = input_block.popleft()
        input_green(t,x,y,green_matrix)
        input_blue(t,x,y, blue_matrix)
        
        score, green_matrix = chk_score_green(score, green_matrix)
        score, blue_matrix = chk_score_blue(score, blue_matrix)
        for a in bl:
            print(a)
        print(score)
        print("-"*20)


main(green_matrix, blue_matrix)