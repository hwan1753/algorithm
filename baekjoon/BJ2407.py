from sys import stdin
import math

n, m = map(int, stdin.readline().split())

print(math.factorial(n) // (math.factorial(n-m) * math.factorial(m)))