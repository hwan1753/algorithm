def solution(m, n, puddles):

    # 매트릭스 제작.
    matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # 출발, 집 좌표
    matrix[1][1] = 1

    # DP 시작
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            # 출발 값
            if y == 1 and x == 1:
                continue
            # 웅덩이가 있는 경우 패쓰
            if [x, y] in puddles:
                matrix[y][x] = 0
            else:
                # 해당 위치 값은 이전값 2개의 합.
                matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]

    return matrix[n][m] % 1000000007