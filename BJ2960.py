import math

N, K = map(int, input().split())
num_arr = [1] * N

prime = [2,3,5,7,11,13]

if N >= 14:
    for num in range(14, N+1):
        chk_num = int(math.sqrt(num))
        chk = True
        for i in range(2, chk_num+1):
            if num % i == 0:
                chk = False
                break

        if chk:
            prime.append(num)

answer = 0
idx = 0
result = 0

while answer < K:
    num = prime[idx]
    delete_num = num
    while delete_num < N + 1:
        if num_arr[delete_num - 1]:
            answer += 1
            result = delete_num
            if answer == K:
                break
            num_arr[delete_num - 1] = 0


            delete_num += num
        else:
            delete_num += num

    idx += 1
print(result)