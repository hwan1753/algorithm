from sys import stdin

N = int(stdin.readline())
arr = []
for num in range(N):
    value = list(map(int,stdin.readline().split()))
    arr.append(value)

answer = []

for value in arr:
    rank = 1
    for compare in arr:
        if value == compare:
            pass
        elif value[0] < compare[0] and value[1] < compare[1]:
            rank += 1
    answer.append(str(rank))
print(" ".join(answer))