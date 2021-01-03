from sys import stdin
import math

def calculation(n, m):
    return (math.factorial(n+m) // (math.factorial(n) * math.factorial(m)))

N, M, K = map(int, stdin.readline().split())

chk = calculation(N, M)
answer = ''
n, m = N, M

if chk < K:
    print(-1)
else:
    while n > 0 and m > 0:
        chk = calculation(n-1, m)

        if chk >= K:
            answer += 'a'
            n -= 1

        else:
            answer += 'z'
            K -= chk
            m -= 1

    answer += 'a' * n + 'z' * m
    print(answer)


# def perm(lst, n):
#     arr = []
#     if n > len(lst):
#         return arr
#
#     if n == 1:
#         for i in lst:
#             arr.append([i])
#     else:
#         for i in range(len(lst)):
#             temp = lst.copy()
#             temp.remove(lst[i])
#             for p in perm(temp, n-1):
#                 arr.append([lst[i]]+p)
#     return arr
#
# def comb(lst, n):
#     arr = []
#     if n > len(lst):
#         return arr
#
#     if n == 1:
#         for i in lst:
#             arr.append([i])
#     else:
#         for i in range(len(lst)-n+1):
#             for temp in comb(lst[i+1:], n-1):
#                 arr.append([lst[i]] + temp)
#     return arr