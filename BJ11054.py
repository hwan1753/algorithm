from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))


if len(arr) == 1:
    print("1")
else:

    answer = 0

    for idx in range(len(arr)):

        left_stack, right_stack = [], []

        for i in range(idx):
            if arr[i] >= arr[idx]:
                continue
            elif left_stack == []:
                left_stack.append(arr[i])
            else:
                if left_stack[-1] < arr[i]:
                    left_stack.append(arr[i])
                else:
                    left_stack[bisect_left(left_stack, arr[i])] = arr[i]
        # print(left_stack)

        for i in range(len(arr) - 1, idx,-1):
            if arr[i] >= arr[idx]:
                continue
            elif right_stack == []:
                right_stack.append(arr[i])
            else:
                if right_stack[-1] < arr[i]:
                    right_stack.append(arr[i])
                else:
                    right_stack[bisect_left(right_stack, arr[i])] = arr[i]


        if right_stack:
            right_stack.append(arr[idx])
        else:
            left_stack.append(arr[idx])
        answer = max(answer, len(left_stack) + len(right_stack))
        # print(left_stack, right_stack)
        # print("-" * 10)
    print(answer)