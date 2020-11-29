from math import sqrt

def solution(nums):
    answer = 0  # 정답값

    for one in range(len(nums)-2):  # 첫번째 숫자
        for two in range(one+1, len(nums)-1):   # 두번째 숫자
            for three in range(two + 1, len(nums)): # 세번째 숫자
                chk_num = nums[one] + nums[two] + nums[three]   # 숫자의 합
                prime = True    # 소수 판별

                if chk_num % 2 == 0 or chk_num % 3 == 0 or chk_num % 5 == 0:    # 2,3 5의 배수인 경우 패스
                    prime = False
                else:
                    # 에라토스테네스의 체 적용
                    for factor in range(2, int(sqrt(chk_num)))+1:
                        if chk_num % factor == 0:
                            prime = False
                            break
                        else:
                            pass
                if prime:
                    # 소수인 경우 정답 + 1
                    answer += 1


    return answer

a = [1,2,3,4, 9, 10, 11]
b = [1,2,7,6,4, 10, 11, 12, 14, 15]
print(solution(a))