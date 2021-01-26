from bisect import bisect_left, bisect_right
import tqdm

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
    # print(len(arr))
    return arr

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
    answer = []

    info_dict = {('-','-','-','-'):[]}

    # language = ('cpp', 'java', 'python','-')
    # part = ('backend','fronted','-')
    # career = ('junior','senior','-')
    # food = ('chkicken','pizza','-')
    info_dict = {}

    for i in info:
        info_arr = i.split()
        info_detail, info_score = [k for k in info_arr[:-1]], int(info_arr[-1]) * -1

        # info_dict[tuple(info_detail)] = info_dict.get(tuple(info_detail), []) + [info_score]
        # for j in range(1, 5):
        #     for temp in comb(info_detail, j):
        #         info_dict[tuple(temp)] = info_dict.get(tuple(temp), []) + [info_score]

        for i in get_type(info_detail):
            if i in info_dict:
                info_dict[i].append(info_score)
            else:
                info_dict[i] = [info_score]

    for key in info_dict.keys():
        info_dict[key].sort()

    for i in query:
        query_arr = i.replace('and',' ').split()
        query_detail, qeury_score = tuple(k for k in query_arr[:-1]), int(query_arr[-1]) * -1

        if len(query_detail) == 0:
            # print(bisect_right(info_dict['all'], qeury_score), info_dict['all'])
            answer.append(bisect_right(info_dict[('all',)], qeury_score))
        else:
            # print(bisect_right(info_dict[query_detail], qeury_score), info_dict[query_detail], qeury_score)
            answer.append(bisect_right(info_dict[query_detail], qeury_score))

    return answer

a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# print(solution(a,b))
# print(comb([1,2,3],1))

a = []
print(bisect_right(a,1))