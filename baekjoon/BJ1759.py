from sys import stdin

def comb(lst, n):
    arr = []
    if n > len(lst):
        return arr

    if n == 1:
        for i in lst:
            arr.append([i])
    else:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:], n-1):
                arr.append([lst[i]] + temp)
    return arr

L, C = map(int, stdin.readline().split())
alphabet = list(stdin.readline().split())
alphabet.sort()
vowels = ['a','e','i','o','u']

candidate = comb(alphabet, L)
for pw in candidate:
    chk1, chk2 = 0, 0
    for c in pw:
        if c in vowels:
            chk1 += 1
        else:
            chk2 += 1
    if chk1 > 0 and chk2 > 1:
        print("".join(pw))