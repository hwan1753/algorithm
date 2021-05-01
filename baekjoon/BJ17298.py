from sys import stdin

N = int(stdin.readline())

num_arr = list(map(int, stdin.readline().split()))

answer = [-1]*N
stack = []

for i in range(len(num_arr)-1, -1, -1):
    # print(i, num_arr[stack[-1]])
    while stack and num_arr[stack[-1]] <= num_arr[i]:
        stack.pop()
    
    if not stack:
        stack.append(i)
    else:
        answer[i] = num_arr[stack[-1]]
        stack.append(i)
answer = [str(i) for i in answer]
print(" ".join(answer))