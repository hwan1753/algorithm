def solution(routes):
    
    chk_camera = [0] * len(routes)      # 총 확인해야하는 차량 수
    count = 0   # 결과값
    routes.sort(key=lambda x:x[1])      # 진출 지점으로 정렬

    for car in range(len(routes)):
        # 만약 해당 차량이 카메라 테스트에서 통과한 경우 패스
        if chk_camera[car]:
            continue
        # 해당 차량이 지나가는 카메라가 없으므로 새로 만듬.
        camera = routes[car][1]
        count +=1
        
        # 새로 만든 카메라가 이후 차량 중에서 지나가는 차량이 있는지 확인
        for num in range(car + 1, len(routes)):
            if routes[num][0] <= camera <= routes[num][1]:
                chk_camera[num] = True

    return count

a = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]

b = [[-2,-1],[1,2],[-3,0]]
c = [[0,0],[1,3],[-10,10],[0,1],[-20,-1]]
d = [[8,13],[-1,1],[0,12],[7,8],[11,11]]
print(solution(a))