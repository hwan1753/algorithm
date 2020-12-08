from sys import stdin

K = int(stdin.readline())
stack = []

for idx in range(K):
    num = int(stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        if stack:
            stack.pop()
print(sum(stack))