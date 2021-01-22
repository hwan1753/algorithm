from sys import stdin
from itertools import chain
import copy

def find_queen(Y, chk_queen):

    if Y == N:
        answer = list(chain(*chk_queen))
        return answer.count(1)

    for j in range(N):
        if chk_queen[Y][j] == 0:
            temp = copy.deepcopy(chk_queen)

            for my in range(N - Y):
                temp[i + my][j] = -1

                if my == 0:
                    for mx in range(N):
                        temp[i+my][mx] = -1
                elif j - my >= 0:
                    temp[i+my][j - my] = -1
                elif j + my < N:
                    temp[i+my][j + my] = -1

            temp[Y][j] = 1
            print(temp)
            return find_queen(Y+1, temp)

    answer = list(chain(*chk_queen))
    return answer.count(1)

N = int(stdin.readline())

stack = []
chk_queen = [[0] * N for _ in range(N)]

answer = 0
for i in range(N):
    answer = max(answer, find_queen(i, chk_queen))
print(answer)