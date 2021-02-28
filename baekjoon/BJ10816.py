from sys import stdin
from bisect import bisect_left, bisect_right

N = int(stdin.readline())
num_arr = sorted(list(map(int, stdin.readline().split())))

M = int(stdin.readline())
result = list()
for i in list(map(int, stdin.readline().split())):
    result.append(bisect_right(num_arr, i) - bisect_left(num_arr, i))


answer = ' '.join(map(str, result))
print(answer)