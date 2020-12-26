from sys import stdin

N = int(stdin.readline())
num_arr = [tuple(map(int,stdin.readline().split())) for _ in range(N)]

num_arr = sorted(num_arr, key=lambda time: (time[1], time[0]))
# print(num_arr)
answer = [num_arr[0]]
now_co = num_arr[0]
for idx in range(1,len(num_arr)):
    if num_arr[idx][0] >= now_co[1]:
        now_co = num_arr[idx]
        answer.append(now_co)
print(len(answer))