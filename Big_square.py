def solution(board):

    # DP를 사용하지 않는 경우 y축 1개 Or x축이 1개
    if len(board[0]) < 2:
        # 만약 1을 포함한다면 최대 1 반환
        if [1] in board:
            return 1
        # 만약 0을 포함한다면 최대 0 반환
        else:
            return 0

    # DP를 사용하므로 1,1 부터 시작
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):

            # 만약 값이 1이라면 DP 실행
            if board[i][j] >= 1:
                # x 이전 값과 y 이전값, x,y이전값(대각선) 중 가장 작은 값 + 1
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    # 전체 값 중에 가장 큰 값이 정사각형을 만족하므로 해당 값 제곱
    return max([num for row in board for num in row]) ** 2

a = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(a))