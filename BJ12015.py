from sys import stdin
from bisect import bisect_left, bisect_right

N = int(stdin.readline())
num_arr = list(map(int,stdin.readline().split()))
answer = [0]

for i in num_arr:
    if answer[-1] < i:
        answer.append(i)
    else:
        answer[bisect_right(answer, i)] = i
a = [1,2,4,7,8,8]
print(bisect_left(a,4))
print(bisect_right(a,4))