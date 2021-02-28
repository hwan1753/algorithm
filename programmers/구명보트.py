import collections

def solution(people, limit):
    answer = 0
    people = collections.deque(sorted(people))
    # print(people)
    idx = len(people) - 1
    while idx > 0:
        chk = people[idx] + people[0]
        if chk <= limit:
            for num in range(1,idx+1):
                chk += people[num]
                if chk <= limit:
                    pass
                else:
                    # print(people)
                    # print(idx, num)
                    # print(chk)
                    answer += 1
                    # del people[idx]
                    for a in range(num):
                        people.popleft()
                    people.pop()
                    idx = len(people) - 1
                    # print(people)
                    break

        else:
            # print(people[idx])
            del people[idx]
            idx = len(people) - 1
            answer += 1
    if len(people) == 1:
        answer += 1
    # print(answer)


    return answer

a = [70, 50, 80, 50,100,40,60]
b = 130
solution(a,b)