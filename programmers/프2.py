import heapq

def solution(t, r):
    answer = []
    now = 0
    end = max(t)

    # heap = []
    chk = []
    while now < end+1:
        # temp = []
        for i in range(len(t)):
            if t[i] == now:
        #         heapq.heappush(heap, (r[i], i))
                chk.append((r[i]*-1,i*-1))
        
        # if heap:
        #     chk = heap[0][0]
        #     while heap and heap[0][0] == chk:
        #         heapq.heappush(temp, heapq.heappop(heap)[1])
            
        #     answer.append(heapq.heappop(temp))
        #     while temp:
        #         heapq.heappush(heap, (chk, temp.pop()))
        print(chk)
        if chk:
            chk.sort(key=lambda x:(x[0],x[1]))
            answer.append(chk.pop()[1] * -1)

        now += 1
    
    # while heap:
    #     answer.append(heapq.heappop(heap)[1])
    chk.sort(key=lambda x:(x[0],x[1]))
    while chk:
        answer.append(chk.pop()[1] * -1)
    
    return answer

a = [7,1,8,1]	
b = [0,1,2,0]	
print(solution(a,b))
