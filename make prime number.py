from math import sqrt

def solution(nums):
    answer = 0

    for one in range(len(nums)-2):
        for two in range(one+1, len(nums)-1):
            for three in range(two + 1, len(nums)):
                chk_num = nums[one] + nums[two] + nums[three]
                prime = True

                if chk_num % 2 == 0 or chk_num % 3 == 0 or chk_num % 5 == 0:
                    prime = False
                else:
                    for factor in range(2, int(sqrt(chk_num)))+1:
                        if chk_num % factor == 0:
                            prime = False
                            break
                        else:
                            pass
                if prime:
                    print(chk_num, nums[one], nums[two], nums[three])
                    answer += 1


    return answer

a = [1,2,3,4, 9, 10, 11]
b = [1,2,7,6,4, 10, 11, 12, 14, 15]
print(solution(a))