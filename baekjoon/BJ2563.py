from sys import stdin

N = int(stdin.readline())

paper = [[0] * 101 for _ in range(101)]

for i in range(N):
    x, y = map(int, stdin.readline().split())
    for iy in range(y, y + 10):
        for ix in range(x, x + 10):
            paper[iy][ix] = 1

answer = 0
for row in paper:
    answer += row.count(1)
print(answer)