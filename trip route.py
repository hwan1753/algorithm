def solution(tickets):

    node_dict = {}      # 노드 hash화
    # 출발지를 key로 도착지를 value로 지정.
    for city in tickets:
        # dict.get(a,b) = dict에서 key가 a인 것을 찾고 없으면 b값을 넣겠다.
        node_dict[city[0]] = node_dict.get(city[0], []) + [city[1]]

    # 알파벳 역순으로 정렬
    for city in node_dict:
        node_dict[city] = sorted(node_dict[city], reverse=True)


    stack = ["ICN"]
    answer = []

    # 스택에 값이 있는동안 계속 반복
    while stack:
        now_city = stack[-1]
        # 만약 해당 도시 출발 항공표가 없을 때 answer에 추가.
        if now_city not in node_dict or node_dict[now_city] == []:
            answer.append(stack.pop())
        else:
            # 해당 도시 출발 항공표가 있을 때 다음 도시 pop해서 스택에 추가
            stack.append(node_dict[now_city].pop())
    # 역순이므로 다시 정렬
    answer.reverse()
    return answer