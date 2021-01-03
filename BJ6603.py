from sys import stdin

def comb(lst, n):
    arr = []
    if len(lst) < n:
        return arr
    if n == 1:
        for i in lst:
            arr.append([i])
    else:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:], n-1):
                arr.append([lst[i]] + temp)

    return arr

while True:
    # input_num = list(map(int,stdin.readline().split()))
    input_num = list(stdin.readline().split())
    if input_num[0] == "0":
        break
    k = input_num[0]
    S = input_num[1:].copy()
    result = comb(S, 6)
    for i in result:
        print(" ".join(i))
    print("")