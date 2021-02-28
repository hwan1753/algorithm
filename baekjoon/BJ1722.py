from sys import stdin
import math
from _collections import deque

def perm(lst, n):
    arr = []
    if n > len(lst):
        return arr
    if n == 1:
        for i in lst:
            arr.append([i])
    else:
        for i in range(len(lst)):
            temp = lst.copy()
            del temp[i]
            for p in perm(temp, n-1):
                arr.append([lst[i]] + p)
    return arr

N = int(stdin.readline())
num_arr = [a for a in range(N+1)]
input_arr = list(map(int, stdin.readline().split()))
if input_arr[0] == 1:
    answer = []
    k = input_arr[1] - 1
    chk_num = N - 1
    for idx in range(N):
        for i in range(1,len(num_arr)):
            loc = math.factorial(chk_num) * i
            if loc > k:

                answer.append(str(num_arr[i]))
                del num_arr[i]
                k -= math.factorial(chk_num) * (i - 1)
                chk_num -= 1

                break
    print(" ".join(answer))
else:
    input_arr = deque(input_arr[1:])
    answer = 0
    del num_arr[0]

    while input_arr:
        num = input_arr.popleft()
        idx = num_arr.index(num)
        # print(num_arr, num)
        if idx != 0:
            answer += math.factorial(len(input_arr)) * idx
            num_arr.remove(num)
        elif len(num_arr) == 1:
            answer += 1
            print(answer)
            break
        else:
            num_arr.remove(num)


#
# print(math.factorial(20))