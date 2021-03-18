from sys import stdin

size_A, size_B = map(int, stdin.readline().split())

A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A_point, B_point = 0, 0
answer = []

while A_point < size_A and B_point < size_B:
    if A[A_point] < B[B_point]:
        answer += [A[A_point]]
        A_point += 1
    else:
        answer += [B[B_point]]
        B_point += 1

if A_point == size_A:
    answer += B[B_point:]
else:
    answer += A[A_point:]

print(" ".join(map(str, answer)))