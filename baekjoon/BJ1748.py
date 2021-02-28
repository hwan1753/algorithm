from sys import stdin

N = int(stdin.readline())

answer = 0
idx = 1
tmp = 0
while True:
    if N // 10 ** idx != 0:
        answer += (10 ** idx - 10 ** (idx-1)) * idx
        idx += 1

    else:
        tmp = (((N - 10 ** (idx-1)) + 1) % (10 ** idx)) * idx
        break
print(answer + tmp)