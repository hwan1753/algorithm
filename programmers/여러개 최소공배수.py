def gcd(a,b):
    while(b!=0):
        r = a % b
        a = b
        b = r
    return a


def solution(arr):
    answer = 1
    arr = sorted(arr)
    if len(arr) == 1:
        # print(arr[0])
        return arr[0]
    elif len(arr) == 2:
        # print("!!{}  {}".format(arr[1],arr[0]))
        least = gcd(arr[1],arr[0])
        # print(arr[1] * arr[0] // least, least)
        return arr[1] * arr[0] // least
    else:
        # print(solution([solution(arr[:len(arr)//2]),solution(arr[len(arr)//2:len(arr)])]))
        return solution([solution(arr[:len(arr)//2]),solution(arr[len(arr)//2:len(arr)])])


a = [2,6,8,14]
b = [1,10,2,3,4,5,6,7,8,9]
c = [12, 16, 9]
solution(a)