def solution(land):

    idx = 1

    while idx < len(land):


        for num in range(len(land[idx])):
            chk = []
            for d_num in range(len(land[idx-1])):
                if num != d_num:
                    chk.append(land[idx][num]+land[idx-1][d_num])

            land[idx][num] = max(chk)


        idx += 1
    return max(land[len(land)-1])


a = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(a))