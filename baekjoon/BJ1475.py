num_arr = [0] * 9

room = list(map(int,input()))

for num in room:
    if num == 9:
        num_arr[6] += 1
    else:
        num_arr[num] += 1

if num_arr[6] % 2 == 1:
    num_arr[6] = (num_arr[6]+1) // 2
else:
    num_arr[6] = num_arr[6] // 2
print(max(num_arr))