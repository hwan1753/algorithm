from _collections import deque

def solution(n, t, m, p):

    original_number = 0

    answer = ""
    people = 0


    while len(answer) < t:
        change_number = ""
        number = original_number

        if number == 0:
            change_number = "0"
        while number > 0:
            remain = number % n

            if remain > 9:
                change_number += chr(55 + remain)
            else:
                change_number += str(remain)

            number = number // n

        queue = deque(list(reversed(change_number)))

        while queue:
            if people % m == p - 1:
                answer += queue.popleft()
                if len(answer) == t:
                    break
            else:
                queue.popleft()

            if people + 1 == m:
                people = 0
            else:
                people += 1

        original_number += 1

    return answer

a = 16
b = 16
c = 2
d = 1

print(solution(a,b,c,d))
# print(len("02468ACE11111111"))