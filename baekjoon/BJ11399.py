N = int(input())

time = list(map(int, input().split()))
time.sort()

total = time[0]
cal_time = 0

for i in range(1,len(time)):
    cal_time += time[i-1]
    total += cal_time + time[i]

print(total)