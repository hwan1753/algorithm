def solution(arr1, arr2):
    # 1번째 매트릭스의 row, col
    arr1_y, arr1_x = len(arr1), len(arr1[0])
    # 2번째 매트릭스의 row, col
    arr2_y, arr2_x = len(arr2), len(arr2[0])

    # 결과 매트릭스 생성
    answer = [[0] * arr2_x for _ in range(arr1_y)]

    # 1번째 매트릭스의 row
    for y_1 in range(arr1_y):
        # 2번째 매트릭스의 col
        for x_2 in range(arr2_x):

            # 1번째 매트릭스의 col == 2번째 매트릭스의 row
            for mul in range(arr1_x):

                answer[y_1][x_2] += arr1[y_1][mul] * arr2[mul][x_2]
    # 결과 매트릭스 return
    return answer

a = [[1, 4], [3, 2], [4, 1]]
b = [[3, 3], [3, 3]]

print(solution(a,b))
