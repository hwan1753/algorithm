from sys import stdin

def binary_search(arr, num):
    # print(arr,num)
    if arr == []:
        return 0
    if len(arr) == 1:
        if arr[0] == num:
            return 1
        else:
            return 0
    m = len(arr)//2
    # print(m)

    if arr[m] == num:
        return 1
    else:
        if arr[m] > num:
            return binary_search(arr[:m], num)
        else:
            return binary_search(arr[m+1:], num)


N = int(stdin.readline())
num_arr = list(map(int, stdin.readline().split()))
num_arr = sorted(num_arr)
M = int(stdin.readline())
chk_arr = list(map(int, stdin.readline().split()))

for m in chk_arr:
    print(binary_search(num_arr, m))