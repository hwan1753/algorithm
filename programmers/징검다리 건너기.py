def solution(stones, k):
    answer = 0

    start, end = 1, 200001
    
    while start <= end:
        
        middle = (start+end) // 2

        chk_stone = True
        count = 0
        for num in stones:
            if num - middle <= 0:
                 count += 1
                 
            else:
                count = 0
            if count == k:
                chk_stone = False
                break
            
        if chk_stone:
            answer = middle
            start = middle+1
        else:
            end = middle - 1

    return answer +1

a = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
b = 3
print(solution(a,b))
