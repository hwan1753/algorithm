def solution(array, commands):
    answer = []
    for num in range(len(commands)):
        tmp = sorted(array[commands[num][0]-1:commands[num][1]])
        # print(tmp)
        answer.append(tmp[commands[num][2]-1])
    return answer

a = [1, 5, 2, 6, 3, 7, 4]
b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(a,b)