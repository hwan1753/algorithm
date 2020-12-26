# 순열 구현
def perm(lst, n):
    arr = []
    if n > len(lst):
        return arr

    if n == 1:
        for i in lst:
            arr.append([i])
    else:
        for i in range(len(lst)):
            temp = [val for val in lst]
            temp.remove(lst[i])
            for p in perm(temp, n-1):
                arr.append([lst[i]]+p)
    return arr
# 조합 구현
def comb(lst, n):
    arr = []

    if n > len(lst):
        return arr

    if n == 1:
        for i in lst:
            arr.append([i])

    else:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:], n-1):
                arr.append([lst[i]] + temp)
    return arr


def solution(relation):
    # 행, 열 정의
    row, col = len(relation), len(relation[0])

    col_arr = [num for num in range(col)]

    candidate_key = []  # 후보키 가능 리스트, 유일성 만족
    key_list = []       # 키 리스트
    result_key = []     # 결과값

    # 조합으로 가능한 키 리스트 추출.
    for num in range(1, col+1):
        key_list.extend(comb(col_arr, num))

    # 키 리스트로 후보키 유일성 체크
    for key_col in key_list:
        check_key = []
        
        # 키가 후보키인지 확인
        for rel in range(row):
            data = ""
            for num in key_col:
                data += relation[rel][num]
            if data not in check_key:
                check_key.append(data)
            else:
                break
                
        # 키가 유일성을 만족.
        if len(check_key) == row:
            # 집합 형태로 추가.
            candidate_key.append(set(key_col))

    # 최소성확인
    for key in candidate_key:
        tmp = True
        if not result_key:
            result_key.append(key)
        else:
            for chk in result_key:
                # 부분집합으로 존재하면 최소성 만족 x
                if chk.issubset(key):
                    tmp = False
                    break
            if tmp:
                result_key.append(key)
    # 최종 후보키 출력
    return len(result_key)

a = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["300", "apeach", "music", "1"]]

b = [["1","2","3","4"],["1","3","3","4"],["2","2","3","5"],["3","3","4",'4']]

print(solution(a))

