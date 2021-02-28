from _collections import deque

def solution(n, edge):
    answer = 1      # 정답값
    now_visit = deque([])   # 방문 노드 큐
    next_visit = []         # 다음 방문 노드
    visited = [0] * (n + 1) # 노드 방문 여부 확인
    visited[1] = 1

    # dictionary를 통해 hash로 빠르게 간선을 찾음.
    node_dic = {}
    for i in range(1,n+1):
        node_dic[i] = []

    for i in edge:
        node_dic[i[0]].append(i[1])
        node_dic[i[1]].append(i[0])

    # 1번 노드부터 시작
    for i in node_dic[1]:
        now_visit.append(i)
        visited[i] = 1
        node_dic[1] = []


    while True:
        # 방문할 노드가 있을때까지 반복
        while now_visit:
            node = now_visit.pop()

            # 해당 노드의 hash값을 통해 다음 방문 노드 확인
            for i in node_dic[node]:
                # 노드 방문 여부 확인
                if visited[i] == 1:
                    continue
                visited[i] = 1
                next_visit.append(i)

        # 다음 방문할 노드가 있으면 계속 진행
        if next_visit:
            now_visit = deque(next_visit)
            answer = len(next_visit)
            next_visit = []
        else:
            # 없는 경우 결과 리턴
            return answer

a = 6
b = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(a,b))