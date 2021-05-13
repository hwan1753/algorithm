from sys import stdin

N, K = map(int, stdin.readline().split())
num_arr = list(map(int, stdin.readline().split()))

chk = [0] * 100001
point_a, point_b = 0, 0
answer, count = 0, 0

while point_a <N:
    while point_b<N and chk[num_arr[point_b]] <K:
        chk[num_arr[point_b]] += 1
        count += 1
        point_b += 1
        
    answer = max(count, answer)
    chk[num_arr[point_a]] -= 1
    count -= 1
    point_a += 1

print(answer)