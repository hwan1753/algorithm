def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    routes = set([costs[0][0]])
    while len(routes) != n:

        for i, cost in enumerate(costs):
            print(i, cost, routes)
            if cost[0] in routes and cost[1] in routes:
                print("!")
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])

    chk_node = [i for i in range(n)]
    count = 0
    for n1, n2, cost in costs:
        if chk_node[n1] != chk_node[n2]:
            temp = chk_node[n2]
            for i in range(n):
                if chk_node[i] == temp:
                    chk_node[i] = chk_node[n1]
            answer += cost
            count += 1
        if count == n - 1:
            break
    return answer
