def solution(n, results):
    matrix = dict()

    for i in range(1, n + 1):
        matrix[i] = [set(), set()]

    for i in results:
        matrix[i[0]][0].add(i[1])
        matrix[i[1]][1].add(i[0])

    for num, match in matrix.items():
        if match[0] and match[1]:
            for win in match[0]:
                matrix[win][1].update(match[1])
            for lose in match[1]:
                matrix[lose][0].update(match[0])

    answer = 0
    for num, match in matrix.items():
        if len(match[0]) + len(match[1]) + 1 == n:
            answer += 1
    return answer