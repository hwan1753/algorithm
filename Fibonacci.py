# def fibonacci(num, num_dict):
#     if num in num_dict:
#         return num_dict[num], num_dict
#     # elif num < 2:
#     #     # print(num)
#     #     return num
#     else:
#         res2, num_dict = fibonacci(num - 2, num_dict)
#         num_dict[num - 2] = res2
#         res1, num_dict = fibonacci(num - 1, num_dict)
#         num_dict[num - 1] = res1
#
#
#         return res1 + res2, num_dict
#
# def solution(n):
#     num_dict = {0:0,1:1}
#     result, _ = fibonacci(n, num_dict)
#     # print(result)
#     return result % 1234567

def solution(n):

    chk = 0     # 피보나치 홀수, 짝수 판별
    fibonacci_num1 = 1  # 피보나치 홀수 번째 값
    fibonacci_num2 = 1  # 피보나치 짝수 번째 값

    idx = 3     # 피보나치 3부터 시작
    
    # n 번째 까지 진행
    while idx < n+1:
        if idx % 2 == 1:    # 홀수 경우
            fibonacci_num1 += fibonacci_num2    # F(n) = F(n-1) + F(n-2)
            chk = 1     # 홀수 체크
        else:               # 짝수 경우
            fibonacci_num2 += fibonacci_num1    # F(n) = F(n-1) + F(n-2)
            chk = 0     # 짝수 체크
        idx += 1    # 숫자 증가


    if chk == 1:    # 홀수면 홀수 F(n)값 리턴
        return fibonacci_num1 % 1234567
    else:           # 짝수면 짝수 F(n)값 리턴
        return fibonacci_num2 % 1234567 

a = 99998
# print(solution(a))
b = 99999
# print(solution(b))
c = 100000
# print(solution(c))

if solution(a) + solution(b) == solution(c):
    print("!!!!!!!")