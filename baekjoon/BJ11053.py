from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())


num_array = list(map(int, stdin.readline().split()))
answer = [num_array[0]]

for num in num_array:
    if num > answer[-1]:
        answer.append(num)
    else:
        answer[bisect_left(answer, num)] = num
print(len(answer))