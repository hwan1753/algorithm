from sys import stdin
from _collections import defaultdict

N, K = map(int, stdin.readline().split())

num_arr = list(map(int, stdin.readline().split()))

R_point = 0
num_dict = defaultdict(int)
answer = 0
for L_point in range(N):
    
    while R_point < N:
        num_dict[num_arr[R_point]] += 1
        if num_dict[num_arr[R_point]] > K:
            
            num_dict[num_arr[L_point]] -= 1
            num_dict[num_arr[R_point]] -= 1
            answer = max(R_point - L_point, answer)
            break
        else:
            R_point += 1
    answer = max(R_point - L_point, answer)
print(answer)