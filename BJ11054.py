from sys import stdin
from bisect import bisect_left, bisect_right


N = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))

if len(arr) == 1:
    print("1")
else:

    answer = 0
    chk_idx = []
    max_val = max(arr)

    for i in range(len(arr)):
        if arr[i] == max_val:
            chk_idx.append(i)


    while chk_idx:
        max_idx = chk_idx.pop()
        left_stack, right_stack = [], []

        if max_idx == 0:
            for i in range(1, len(arr)):
                if right_stack == []:
                    right_stack.append(arr[i])
                else:
                    if right_stack[-1] > arr[i]:
                        right_stack.append(arr[i])
                    elif right_stack[-1] < arr[i]:
                        if arr[i] != max_val:
                            right_stack[bisect_left(right_stack, arr[i]) - 1] = arr[i]
                            # print(bisect_left(right_stack, arr[i]), arr[i], right_stack)
        # elif max_idx == N - 1:
        #     for i in range(n - 2, )
        print(right_stack)