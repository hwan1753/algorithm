from sys import stdin

N = int(stdin.readline())

arr = []
dic = {}
for idx in range(N):
    number = int(stdin.readline())
    arr.append(number)
    if number not in dic:
        dic[number] = 1
    else:
        dic[number] +=1
mean = round(sum(arr) / N)
center = sorted(arr)[N // 2]

maximum = []

for a, b in dic.items():
    if b == max(dic.values()):
        maximum.append(a)


print(mean)
print(center)
if len(maximum) > 1:
    print(sorted(maximum)[1])
else:
    print(maximum[0])
print(max(arr)-min(arr))