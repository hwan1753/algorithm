from itertools import chain

def solution(n):

    result = []
    for a in range(1,n+1):
        result.append([0 for b in range(a)])

    count = 1 # 횟수로 결국 n 번까지
    row = 0 # 각 배열 층 수
    col = 1
    st = [0,n-1] # 1번째 면 들어가는 위치
    mid = [1,n-1]
    end = [-1,1] # 3번째 면 들어가는 위치
    val = 1 # 각 들어가는 숫자
    # print(result)
    while count < n+1:

        if count % 3 == 1:
            result[row][st[0]] = val
            # print(result)
            val += 1
            row += 1
            if row > st[1]:
                row -= 1
                st[0] += 1
                st[1] -= 1
                count += 1
                # print(count)
        elif count % 3 == 2:
            result[row][col] = val
            # print(result)
            val += 1
            col += 1
            if col > mid[1]:
                mid[0] += 1
                mid[1] -= 2
                row -= 1
                col = mid[0]
                count += 1
                # print(count)
        elif count % 3 == 0:
            result[row][end[0]] = val
            # print(result)
            val += 1
            row -= 1
            if row < end[1]:
                row += 2
                end[0] -= 1
                end[1] += 2
                count += 1
    # print(result)
    return list(chain(*result))


a = 6
print(solution(a))