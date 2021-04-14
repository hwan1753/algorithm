from sys import stdin
from pprint import pprint

N, M = map(int, stdin.readline().split())
school = [''] + list(map(str,stdin.readline().split()))

def get_parent(arr, num):
    if parent[num] == num:
        return num
    parent[num] = get_parent(parent, parent[num])
    return parent[num]

def union_parent(arr, num_a, num_b):
    
    a = get_parent(arr, num_a)
    b = get_parent(arr, num_b)

    arr[b] = a

    return arr

def chk_school(school_a, school_b):
    return school[school_a] != school[school_b]


node_arr = []
parent = [i for i in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, stdin.readline().split())
    node_arr += [[weight, start, end]]
    
node_arr.sort(key=lambda x:x[0])

num = 0
idx = 0
res = []

while idx < M and len(res) < N-1:
    weight, start, end = node_arr[idx]
    
    if chk_school(start, end) and get_parent(parent, start) != get_parent(parent, end):
        
        parent= union_parent(parent, start, end)
        res.append(weight)
    
    idx += 1

if len(res) == N-1:
    print(sum(res))
else:
    print(-1)
