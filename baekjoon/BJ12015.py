from sys import stdin
from bisect import bisect_left, bisect_right

N = int(stdin.readline())
num_arr = list(map(int,stdin.readline().split()))
answer = [0]

for i in num_arr:
    if answer[-1] < i:
        answer.append(i)
    else:
        answer[bisect_left(answer, i)] = i
print(len(answer)-1)