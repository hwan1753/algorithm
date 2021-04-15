from sys import stdin

N, M, t = map(int, stdin.readline().split())


node_arr = []
for _ in range(M):
    start, end, weight = map(int, stdin.readline().split())
    node_arr.append([weight, start, end])

node_arr.sort(key=lambda x:x[0])

def get_parent(arr, num):
    
    if arr[num] == num:
        return num
    arr[num] = get_parent(arr, arr[num])
    return arr[num]

def union_parent(arr, num_a, num_b):
    a = get_parent(arr, num_a)
    b = get_parent(arr, num_b)

    arr[b] = a
    return arr

parent = [i for i in range(N+1)]
idx = 0
result = []

while idx < M:
    weight, num_a, num_b = node_arr[idx]

    if get_parent(parent, num_a) != get_parent(parent, num_b):
        union_parent(parent, num_a, num_b)
        result.append(weight + t*len(result))

    idx += 1

if len(result) == N-1:
    print(sum(result))
    