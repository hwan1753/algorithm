from sys import stdin

n = int(stdin.readline())

answer = [1,3]
for i in range(2, n):
    answer.append(answer[i-2] + answer[i-1] + answer[i-1])
print(answer[-1])