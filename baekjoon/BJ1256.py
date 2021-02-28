from sys import stdin
import math

# 중복 있는 순열 계산 하는 방법 n+m! / (n! * m!)
def calculation(n, m):
    return (math.factorial(n+m) // (math.factorial(n) * math.factorial(m)))

# a 갯수, z 갯수, K번째 값
N, M, K = map(int, stdin.readline().split())

# N+M개 전부 있을때 갯수
chk = calculation(N, M)
answer = ''
n, m = N, M

# 만약 K가 N+M 전부있을때 보다 많으면 -1
if chk < K:
    print(-1)
else:
    # chk 계산해서 K를 기준으로 문자열 하나씩 찾아가는 과정
    while n > 0 and m > 0:
        chk = calculation(n-1, m)
        # 만약 K보다 큰 경우는 a
        if chk >= K:
            answer += 'a'
            n -= 1
        # k 보다 작은 경우는 z
        else:
            answer += 'z'
            K -= chk
            m -= 1
    # 남은 a 혹은 z 추가
    answer += 'a' * n + 'z' * m
    print(answer)