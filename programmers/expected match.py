def solution(n,a,b):
    answer = 1  # 정답값

    while True:     # 리턴할 때 까지 반복
        # 두 값의 차이가 1의 차이가 날때
        # 주의) a와 b가 대진을 해야하는데 2,3 같이 1의 차이가 나도 대결 안하는 경우
        if abs(a - b) == 1 and a // 2 != b // 2:
            return answer   # 정답 리턴
        else:
            if a % 2 == 1:  # 홀수일 때
                a = (a + 1) // 2
            else:
                a = a // 2  # 짝수일 때

            if b % 2 == 1:
                b = (b + 1) // 2    # 홀수일 때
            else:
                b = b // 2      # 짝수일 때
            answer += 1     # 대진횟수



n = 512
a = 2
b = 3
print(solution(n,a,b))