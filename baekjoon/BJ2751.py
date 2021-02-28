from sys import stdin

def quick_sort(arr, low, high):
    print(arr)
    if len(arr) == 1:
        return arr

    pivot = arr[0]
    low_num, high_num = None, None

    while low <= high:
        if arr[low] < pivot:
            low += 1
        else:
            low_num = arr[low]
        if arr[high] > pivot:
            high -= 1
        else:
            high_num = arr[high]

        if low_num and high_num:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
            low += 1
            high -= 1

    arr_mid = [pivot]
    arr[0] = arr[high]


    if high == 0:

        arr_back = quick_sort(arr[low:], 1, len(arr[low:])-1)
        return arr_mid + arr_back
    elif low == len(arr):
        arr_front = quick_sort(arr[:high],1,len(arr[:high])-1)
        return arr_front + arr_mid
    else:
        arr_front = quick_sort(arr[:high],1,len(arr[:high])-1)
        arr_back =  quick_sort(arr[low:], 1, len(arr[low:])-1)
        print(arr_front + arr_mid + arr_back)
        return arr_front + arr_mid + arr_back

def merge_sort(arr):

    if len(arr) <= 1:

        return arr

    mid = len(arr) // 2
    front = merge_sort(arr[:mid])
    back = merge_sort(arr[mid:])
    # print(front, back)
    idx, i1, i2 = 0, 0, 0

    while i1 < len(front) and i2 < len(back):

        if front[i1] < back[i2]:
            arr[idx] = front[i1]
            i1 += 1
            idx += 1
        else:
            arr[idx] = back[i2]
            i2 += 1
            idx += 1

    if i1 == len(front):
        while i2 < len(back):
            arr[idx] = back[i2]
            idx += 1
            i2 += 1

    elif i2 == len(back):
        while i1 < len(front):
            arr[idx] = front[i1]
            idx += 1
            i1 += 1
    return arr

# N = int(stdin.readline())
# # num_arr = [int(stdin.readline()) for _ in range(N)]
# num_arr = []
# #
# for i in range(N):
#     num_arr.append(int(stdin.readline()))
# # print(num_arr)
# res = merge_sort(num_arr)
#
# # low, high = 1, len(num_arr) - 1
# # res = quick_sort(num_arr, low, high)
#
# for i in res:
#     print(i)

n=int(input())
num = [int(input()) for _ in range(n)]

# for _ in range(n):
#     num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)