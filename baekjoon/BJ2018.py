N = int(input())

answer = 0
point_a, point_b = 1,1
temp = point_b

while point_a < N+1:
    while point_b<N+1 and temp <=N:
        if temp == N:
            # print(point_a, point_b)
            answer += 1

        point_b += 1
        temp += point_b

    temp -= point_a
    point_a += 1
    
print(answer)
