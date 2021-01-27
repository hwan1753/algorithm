from bisect import bisect_right

def get_type(type_arr):
    arr = []
    # 0개 '-'
    arr.append(tuple(type_arr))
    # 1개 '-'
    for i in range(4):
        temp = type_arr[:]
        temp[i] = '-'
        arr.append(tuple(temp))
    # 2개 '-'
    for i in range(4):
        for j in range(i+1, 4):
            temp = type_arr[:]
            temp[i] = '-'
            temp[j] = '-'
            arr.append(tuple(temp))
    # 3개 '-'
    for i in range(4):
        for j in range(i+1,4):
            for k in range(j+1,4):
                temp = type_arr[:]
                temp[i] = '-'
                temp[j] = '-'
                temp[k] = '-'
                arr.append(tuple(temp))
    # 4개 '-'
    arr.append(('-','-','-','-'))
    return arr

# 조합 구현
def comb(lst, n):
    arr = []
    if len(lst) < n:
        return arr

    if n == 1:
        for i in lst:
            arr.append([i])
    else:
        for i in range(len(lst)-n + 1):
            for temp in comb(lst[i+1:], n-1):
                arr.append([lst[i]] + temp)
    return arr

def solution(info, query):

    answer = [] # 결과값
    info_dict = {}  # info에 대한 정리.

    # info값 정리
    for i in info:

        info_arr = i.split()
        # 이분 탐색할 때 큰 값부터 시작하기 위해서 -1을 곱함.
        info_detail, info_score = [k for k in info_arr[:-1]], int(info_arr[-1]) * -1
        # 조합으로 16개를 구하는 방법.
        # info_dict[tuple(info_detail)] = info_dict.get(tuple(info_detail), []) + [info_score]
        # for j in range(1, 5):
        #     for temp in comb(info_detail, j):
        #         info_dict[tuple(temp)] = info_dict.get(tuple(temp), []) + [info_score]

        # 단순히 16개를 구하는 방법
        for i in get_type(info_detail):
            if i in info_dict:
                info_dict[i].append(info_score)
            else:
                info_dict[i] = [info_score]

    # 이분탐색을 하기위해서 sorting
    for key in info_dict.keys():
        info_dict[key].sort()

    # query문 계산
    for i in query:
        # and를 없애고 빈칸 기준으로 나누기
        query_arr = i.replace('and','').split()
        # 가장 마지막값은 제외하고 tuple로 만들고, score는 이분탐색시 빠르게 큰 값부터 시작해서 -1을 곱함.
        query_detail, qeury_score = tuple(k for k in query_arr[:-1]), int(query_arr[-1]) * -1

        # 해당 쿼리문이 없는 경우.
        if query_detail not in info_dict:
            answer.append(0)
        # 해당 쿼리문이 있는 경우 info_dict에서 쿼리문 찾은 이후
        # 이분탐색해서 해당 값이 들어갈 수 있는 가장 끝값 append에 추가하기
        else:
            answer.append(bisect_right(info_dict[query_detail], qeury_score))

    return answer

a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a,b))