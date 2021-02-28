from sys import stdin

N, C = map(int, stdin.readline().split())

house = []
for n in range(N):
    house.append(int(stdin.readline()))

house = sorted(house)

start = house[1]-house[0]
end = house[-1] - house[0]

for num in range(1,len(house)):
    if house[num] - house[num-1] < start:
        start = house[num] - house[num-1]



result =0

while start <= end:
    mid = (start + end) // 2
    # print(mid)
    chk_house = house[0]
    idx = 1
    chk = 1
    while idx < len(house):
        if house[idx] - chk_house >= mid:
            chk_house = house[idx]

            chk += 1
        idx += 1


    if chk >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)