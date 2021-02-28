from sys import stdin
import math

T = int(stdin.readline())

for i in range(T):
    N, M = map(int, stdin.readline().split())
    print(math.factorial(M) // (math.factorial(N) * math.factorial(M-N)))