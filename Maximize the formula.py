from _collections import deque

def solution(expression):
    # 
    priority = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    answer = 0
    arr = deque([])

    num = ''
    for ch in expression:
        if ch.isnumeric():
            num += ch
        else:
            arr.append(int(num))
            num = ''
            arr.append(ch)
    arr.append(int(num))


    for formular in priority:
        queue = arr.copy()
        for operator in formular:
            calculate = deque([])
            while len(queue) > 0:
                chk = queue.popleft()
                if chk == operator:
                    if chk == '+':
                        num1 = calculate.pop()
                        num2 = queue.popleft()
                        calculate.append(num1+num2)
                    elif chk == '-':
                        num1 = calculate.pop()
                        num2 = queue.popleft()
                        calculate.append(num1 - num2)
                    else:
                        num1 = calculate.pop()
                        num2 = queue.popleft()
                        calculate.append(num1 * num2)
                else:
                    calculate.append(chk)

            queue = calculate.copy()

        # print(queue)
        result_num = queue.pop()
        if abs(result_num) > answer:
            answer = abs(result_num)

    return answer

a = "100-200*300-500+20"
b = "50*6-3*2"
print(solution(a))
