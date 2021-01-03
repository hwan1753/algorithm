from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

start, end = 1, N ** 2
# start, end = 1, N
answer = 0
while start <= end:
    middle = (start + end) // 2
    count = 0
    for i in range(1, N+1):
        count += min(middle//i, N)

    if count >= K:
        end = middle - 1
        answer = middle
    else:
        start = middle + 1
print(answer)
print(start)