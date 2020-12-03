def solution(n,a,b):
    answer = 1

    while True:

        if abs(a - b) == 1 and a // 2 != b // 2:
            return answer
        else:
            if a % 2 == 1:
                a = (a + 1) // 2
            else:
                a = a // 2

            if b % 2 == 1:
                b = (b + 1) // 2
            else:
                b = b // 2
            answer += 1



n = 512
a = 2
b = 3
print(solution(n,a,b))