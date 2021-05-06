def solution(gems):
    answer = []
    gem_list = set(gems)
    chk_gem = {gem:0 for gem in gem_list}

    start, end, count = 0, 0, 0
    temp = [0, 1e9]

    while end < len(gems) and start < len(gems):
        now = gems[end]
        chk_gem[now] += 1
        chk = False
        if chk_gem[now] == 1:
            count += 1
        while count == len(gem_list) and start < len(gems):
            
            if chk_gem[gems[start]] != 1:
                chk_gem[gems[start]] -= 1
                
            elif chk_gem[gems[start]] == 1:
                chk_gem[gems[start]] -= 1
                count -= 1
            start += 1
            chk = True
        if chk and temp[1] - temp[0] > end+1 - start:
            temp = [start, end+1]
            
            
        if end < len(gems):
            end += 1
        else:
            start = len(gems)
    
    return temp

a = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY"]
print(solution(a))
b = ["XYZ", "XYZ", "XYZ"]	
print(solution(b))
