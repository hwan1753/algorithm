from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

direct_friend = []
second_friend = {}

answer = {}

for n in range(2,N+1):
    second_friend[n] = []

for m in range(M):
    f1, f2 = map(int, stdin.readline().split())
    if f1 == 1:
        direct_friend.append(f2)
    else:
        second_friend[f1].append(f2)
        second_friend[f2].append(f1)

for f in direct_friend:
    answer[f] = 1
    if f in second_friend:
        for se in second_friend[f]:
            answer[se] = 1
print(len(answer))
