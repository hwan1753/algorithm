from sys import stdin

N = int(stdin.readline())

distance = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
answer = 0

min_cost = cost[0]

for i in range(len(distance)):

    min_cost = min(min_cost, cost[i])
    answer += distance[i] * min_cost
    # print(min_cost, answer)
print(answer)