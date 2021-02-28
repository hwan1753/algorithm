def solution(citations):
    a = sorted(citations)
    result = 0
    print(a)

    for idx in range(len(a)-1,-1,-1):
        if idx < a[len(a) - idx - 1]:
            result = idx + 1
            print(result)
            return result
    return result

a = [3,10,111,1,2,4,8, 7,142, 155]
b  = [5,5,5,4,7,7,7,7,7,3,10]
c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
solution(c)