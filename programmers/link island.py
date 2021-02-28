def solution(n, costs):
    answer = 0
    # 간선의 크기로 정렬
    costs.sort(key=lambda x: x[2])
    # union-find를 set으로 설정
    routes = set([costs[0][0]])

    # 모든 노드를 연결한 경우 멈춤.
    while len(routes) != n:

        for i, cost in enumerate(costs):
            # 만약 시작노드와 마지막 노드가 연결되면 싸이클이 발생하는 경우
            if cost[0] in routes and cost[1] in routes:
                continue
            # 싸이클이 발생하지 않는 경우
            if cost[0] in routes or cost[1] in routes:
                # set 새로고침
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                # 반영된 간선을 시각적으로 보기 편하게 하기위해 삽입(없어도 됨)
                costs[i] = [-1, -1, -1]
                break
    return answer


def solution(n, costs):
    answer = 0
    # 간선의 크기로 정렬
    costs.sort(key=lambda x: x[2])
    # union-find를 배열로 설정
    chk_node = [i for i in range(n)]
    count = 0 # 크루스칼을 만족하는 경우 간선의 갯수는 노드 -1
    for n1, n2, cost in costs:
        # 만약 시작노드와 마지막 노드가 연결되면 싸이클이 발생하는 경우
        if chk_node[n1] != chk_node[n2]:
            # 끝 노드 union-find 실행
            temp = chk_node[n2]
            for i in range(n):
                if chk_node[i] == temp:
                    chk_node[i] = chk_node[n1]

            answer += cost
            count += 1
        if count == n - 1:
            break
    return answer
