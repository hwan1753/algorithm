from sys import stdin

answer = 0
N = int(stdin.readline())
for num in range(N):
    c_arr = []
    word = stdin.readline()
    res = True

    for c in word:
        if not c_arr:
            c_arr.append(c)
        else:
            if c_arr[-1] != c and c not in c_arr:
                c_arr.append(c)
            elif c_arr[-1] != c and c in c_arr:
                res = False
                break
    if res:
        answer += 1
print(answer)