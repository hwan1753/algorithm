from itertools import chain

def solution(s):
    answer = [] # 결과값
    arr = []    # 문자를 배열로 변환

    k = []      # 숫자를 임시로 저장
    tmp = ""    # 숫자값


    # 문자 입력값을 배열로 변환
    for i in s:

        if i.isnumeric():   # 값이 숫자인지 확인하여 숫자값 저장
            tmp += i
        elif i == "," and tmp != "":    # 숫자값 배열에 입력
            k.append(int(tmp))
            tmp = ""
        elif i == "}"and tmp != "":     # } 값을 기준으로 집합 분리
            k.append(int(tmp))
            arr.append([len(k),k])      # 집합의 크기와 집합 저장

            tmp = ""
            k = []


    for x in sorted(arr):       # 집합의 크기로 정렬
        answer.append(x[1])
    answer = list(chain(*answer))   # 1차원 배열로 변형

    res = []
    for x in answer:
        if x not in res:
            res.append(x)

    return res

a = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(a))
