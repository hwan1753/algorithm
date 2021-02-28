def solution(n, results):
    # 선수 경기 결과 hash로 저장
    matrix = dict()

    # 이기는 사람 집합과 지는 사람 집합
    for i in range(1, n + 1):
        matrix[i] = [set(), set()]

    # 경기 결과 입력
    for i in results:
        matrix[i[0]][0].add(i[1])
        matrix[i[1]][1].add(i[0])

    # 만약 A > B 이고 B > C 인경우 A>C인 관계(>는 이긴다)
    # 모든 선수를 통해 경기하지 않아도 결과를 아는 경우 저장.
    for num, match in matrix.items():
        if match[0] and match[1]:
            for win in match[0]:
                matrix[win][1].update(match[1])
            for lose in match[1]:
                matrix[lose][0].update(match[0])

    # 만약 이기는 경우, 지는 경우, 자기 자신의 합이 모든 선수의 수인 경우 +1
    answer = 0
    for num, match in matrix.items():
        if len(match[0]) + len(match[1]) + 1 == n:
            answer += 1
    return answer