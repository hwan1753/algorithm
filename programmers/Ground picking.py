def solution(land):

    # 2번째 층부터 시작하므로 1로 시작
    idx = 1

    # DP 시작
    while idx < len(land):
        # 4개의 숫자 확인.
        for num in range(len(land[idx])):
            chk = []    # 임의의 배열.
            for d_num in range(len(land[idx-1])):
                if num != d_num:
                    # 위의 칸과 다를 때, 위의 층과의 합.
                    chk.append(land[idx][num]+land[idx-1][d_num])
            # 해당 칸에서 나올 수 있는 가장 높은 값.
            land[idx][num] = max(chk)
        # 층수 + 1
        idx += 1
    return max(land[len(land)-1])


a = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(a))