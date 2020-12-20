from sys import stdin

def search(arr, top, bottom, m):
    if top < bottom:
        return top

    mid = (top + bottom) // 2
    # print(mid)
    total = 0

    for x in range(len(arr)):
        if arr[x] > mid:
            total += arr[x] - mid
    # print(total)

    if total >= m:
        bottom = mid + 1
        # print(top, bottom)
        return search(arr,top,bottom,m)

    else:
        top = mid - 1
        # print(top, bottom)
        return search(arr, top, bottom, m)

N, M = map(int, stdin.readline().split())

tree_arr = list(map(int,stdin.readline().split()))
bottom, top = 1, max(tree_arr)
print(search(tree_arr, top, bottom, M))

bottom, top = 1, max(tree_arr)
while top >= bottom:
    mid = (top+bottom) // 2

    total = 0
    for i in tree_arr:
        if i > mid:
            total += i - mid

    if total >= M:
        bottom = mid + 1
    else:
        top = mid - 1
print(top)

