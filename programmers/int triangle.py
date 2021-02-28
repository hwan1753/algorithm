def solution(triangle):
    # DP로 2번째 줄부터 시작
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            # 비교할 2가지 값.
            calculation1, calculation2 = triangle[row][col], triangle[row][col]
            # idx -1 위치에서 내려온 것.
            if 0 <= col - 1 < len(triangle[row - 1]):
                calculation1 += triangle[row - 1][col - 1]
            # idx 위치에서 내려온 것.
            if 0 <= col < len(triangle[row - 1]):
                calculation2 += triangle[row - 1][col]
            # 둘 중 큰 값 선택
            triangle[row][col] = max(calculation1, calculation2)
    # 마지막 줄에서 가장 큰 값 선택
    return max(triangle[-1])