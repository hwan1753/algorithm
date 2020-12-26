def solution(N, number):
    answer = 1
    arr = [set() for x in range(8)]

    if N == number:
        return answer

    for i in range(1,9):
        arr[i-1].add(int(str(N) * i))

    for i in range(1,8):
        for j in range(i):
            for num1 in arr[j]:
                for num2 in arr[i - j - 1]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2 != 0:
                        arr[i].add(num1 // num2)
        if number in arr[i]:
            answer = i + 1
            return answer


    return -1

a = 7
b = 7776
print(solution(a,b))