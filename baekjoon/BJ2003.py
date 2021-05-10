from sys import stdin

N, M = map(int, stdin.readline().split())
num_arr = list(map(int,stdin.readline().split()))

start, end = 0, 0
chk = 0
answer = 0

while end < N:
    while chk < M and end < N:
        chk += num_arr[end]
        end += 1

    while chk > M:
        chk -= num_arr[start]
        start += 1
    if chk == M:
        answer += 1
        chk -= num_arr[start]
        start += 1
    
print(answer)
        
