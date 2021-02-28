def solution(nums):
    count =len(nums) // 2
    num_dict = {}
    for i in nums:
        if i not in num_dict:
            num_dict[i] = 1
    if count < len(num_dict):
        return count
    else:
        return len(num_dict)


a = [3,1,2,3]
print(solution(a))