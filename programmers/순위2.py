def solution(n, results):
    answer = 0
    player = {i:[set(),set()] for i in range(1,n+1)}

    for i, j in results:
        
        player[i][0].add(j)
        player[j][1].add(i)

    for idx, match in player.items():
        if match[0] and match[1]:
            for win in match[0]:
                player[win][1].update(match[1])
            for lose in match[1]:
                player[win][0].update(match[0])
        
    
    for i in range(1,n+1):
        if len(player[i][0]) + len(player[i][1]) == n-1:
            answer += 1
    return answer
    
a = 5
b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(a,b))