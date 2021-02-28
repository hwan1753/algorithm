def solution(record):

    queue = record.copy()  # record를 queue로 복사
    user = {}       # User uid, 닉네임 저장
    result = []     # 결과값
    chk = []        # 행동과 uid 저장 
    idx = 0         # queue 인텍스 값
    
    # 모든 값 탐색
    while idx < len(queue):
        # 행동, uid, 닉네임을 구분
        value = list(map(str,queue[idx].split()))
        # 입장한 경우
        if value[0] == "Enter":
            # 행동, uid 저장
            chk.append([value[0],value[1]])
            # dict에 uid, 닉네임 저장
            user[value[1]] = value[2]
        # 닉네임 변경한 경우
        elif value[0] == "Change":
            # dict에 닉네임 변경
            user[value[1]] = value[2]
        # 나간 경우
        else:
            # 행동, uid 저장
            chk.append([value[0], value[1]])
        idx += 1
    # 저장한 chk를 통해 차례대로 출력        
    for num in range(len(chk)):
        if chk[num][0] == "Enter":
            result.append(user[chk[num][1]] + "님이 들어왔습니다.")
        else:
            result.append(user[chk[num][1]] + "님이 나갔습니다.")
    return result