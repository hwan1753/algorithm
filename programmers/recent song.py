def solution(m, musicinfos):
    answer = ["(None)",-1]
    m = list(str(m))
    word = 0

    # "#"합치기
    while word < len(m):
        if m[word] == "#":
            m[word - 1] += "#"
            del m[word]
        else:
            word += 1

    # 시간 계산
    for music in musicinfos:
        arr = music.split(',')  # 시작, 종료, 노래, 계이름
        start, end = arr[0].split(':'), arr[1].split(':')   # 시간 확인
        start_hour, start_min = int(start[0]), int(start[1])    # 시작 시작
        end_hour, end_min = int(end[0]), int(end[1])        # 종료 시간

        hour, min =  end_hour - start_hour, end_min - start_min # 플레이 시간

        time = hour * 60 + min + 1  # 시간 -> 분

        name = arr[2]   # 노래 제목
        scale = list(str(arr[3]))   # 음계
        chk = 0
        # "#" 합치기
        while chk < len(scale):
            if scale[chk] == "#":
                scale[chk - 1] += "#"
                del scale[chk]
            else:
                chk += 1

        idx = 0
        res = []
        # 시간 만큼 계이름 입력
        while idx < time:
            res.append(scale[idx % len(scale)])
            idx += 1


        loc = 0     # 체크 시작 위치
        # 시작위치 처음부터 끝까지 확인
        while loc < len(res) - len(m):
            correct = True  # 일치여부 확인
            for c in range(len(m)):
                # m 과 계이름 확인
                if res[loc+c] != m[c]:
                    correct = False
                    break

            # 일치하면 재생 시간 계산.
            if correct:
                if answer[1] < time:
                    answer = [name, time]
                    break
            loc += 1
    
    return answer[0]    # 이름 출력




a = "ABC"
b = ["11:58,12:14,HELLO,C#DEFGA", "12:50,13:05,WORLD,ACDEF"]
print(solution(a,b))