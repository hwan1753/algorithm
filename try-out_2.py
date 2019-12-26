import math
from decimal import Decimal

A = input().split(' ')
n = int(A[0])
k = int(A[1])

if n >= 1 and n <=500 and k >=1 and k <=n:
    average1, average2, var, dev = 0, 0, 0, 0
    min1= Decimal('INF')
    num = list(map(int,input().split(' ')))
    for s in range(n - k + 1):
        sum_val = sum(num[s:s + k - 1])
        sum_val_sq = sum([v * v for v in num[s:s + k - 1]])

        # 길이 변경
        for l in range(k, n - s + 1):
            sum_val += num[s + l - 1]
            sum_val_sq += num[s + l - 1] ** 2
            aver = sum_val / Decimal(l)
            std = (sum_val_sq / Decimal(l) - aver ** 2).sqrt()

            min1 = min(min1, std)
    print('%.11f' % min1)