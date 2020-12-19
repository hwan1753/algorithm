from sys import stdin

def combination(lst, num):
    arr = []
    if num > len(lst):
        return arr

    if num == 1:
        for i in lst:
            arr.append([i])
    elif num > 1:
        for i in range(len(lst) - num + 1):
            for temp in combination(lst[i+1:], num - 1):
                arr.append([lst[i]]+temp)
    return arr

N, M = map(int, stdin.readline().split())

chicken = []
home = []
minimum = 999
for n in range(N):
    arr = list(map(int, stdin.readline().split()))
    for i in range(len(arr)):
        if arr[i] == 2:
            chicken.append((n, i))
        elif arr[i] == 1:
            home.append((n, i))

chicken_comb = combination(chicken, M)

minimum = 9999
for case in chicken_comb:
    total = 0
    for loc in home:
        cal = 9999
        for chi in case:
            chk = abs(chi[0] - loc[0]) + abs(chi[1] - loc[1])
            if cal > chk:
                cal = chk
        total += cal
    if minimum > total:
        minimum = total

print(minimum)