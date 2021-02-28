from sys import stdin

N, M = map(int,stdin.readline().split())

square = [list(str(input())) for _ in range(N)]

num = 1

res = 1


while num < min(N,M):
    for y in range(N-num):
        for x in range(M-num):
            ay, ax = y + num, x + num
            if ay < N and ax < M:
                if int(square[y][x]) == int(square[ay][x]) == int(square[y][ax]) == int(square[ay][ax]):
                    total = (ay - y + 1) * (ax - x + 1)
                    if total > res:
                        res = total
                        # print(y,x,num)

    num += 1
print(res)
