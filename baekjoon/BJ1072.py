from sys import stdin
import math

X, Y = map(int, stdin.readline().split())

original = math.floor(100 * Y / X)

start, end = 1, 1000000000
answer = -1
while start <= end:
    middle = (start + end) // 2
    # print(middle, start, end)
    # print(math.floor((Y + middle) / (X + middle) * 100), original)
    if math.floor(100 * (Y+middle) / (X+middle)) > original:
        answer = middle
        end = middle - 1
    else:
        start = middle + 1

print(answer)
print(original)
print(math.floor((Y+answer) / (X+answer) * 100))