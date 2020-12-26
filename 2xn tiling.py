import math

def perm(lst, n):
    arr = []

    if len(lst) < n:
        return arr

    if n == 1:
        for i in lst:
            arr.append([i])

    else:
        for i in range(len(lst)):
            temp = [val for val in lst]
            temp.remove(lst[i])
            for p in perm(temp,n-1):
                arr.append([lst[i]] + p)

def solution(n):
    # answer = 1
    # count_one = n - 2
    # count_two = 1
    #
    # while count_one > 1:
    #
    #     answer += math.factorial(count_one+count_two) // (math.factorial(count_one) * math.factorial(count_two))
    #     count_one -= 2
    #     count_two += 1
    #
    #     # print(answer)
    #     # print(count_one, count_two)
    # if count_one == 1:
    #     answer += math.factorial(count_one + count_two) // (math.factorial(count_one) * math.factorial(count_two))
    # else:
    #     answer += 1
    answer = 1
    start1 = 1
    start2 = 2

    num = 2
    while num < n:
        answer = start1 + start2
        start1 = start2
        start2 = answer
        num += 1
    return answer % 1000000007

a = 60000
print(solution(a))
