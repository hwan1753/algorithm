def solution(arr1, arr2):
    arr1_y, arr1_x = len(arr1), len(arr1[0])
    arr2_y, arr2_x = len(arr2), len(arr2[0])
    answer = [[0] * arr2_x for _ in range(arr1_y)]

    for y_1 in range(arr1_y):

        for x_2 in range(arr2_x):
            for mul in range(arr1_x):

                answer[y_1][x_2] += arr1[y_1][mul] * arr2[mul][x_2]

    return answer

a = [[1, 4], [3, 2], [4, 1]]
b = [[3, 3], [3, 3]]

print(solution(a,b))
