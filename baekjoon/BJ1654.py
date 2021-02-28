from sys import stdin

K, N = map(int, stdin.readline().split())

num_arr = []
for n in range(K):
    num_arr.append(int(stdin.readline()))

start, end = 1, max(num_arr)


while start <= end:
    answer = 0
    mid = (start + end) // 2
    # print(start, end, mid)
    for i in num_arr:
        answer += i // mid
    # print(answer)
    if answer >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)