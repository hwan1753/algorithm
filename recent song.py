def solution(m, musicinfos):
    answer = ["(None)",-1]
    m = list(str(m))
    word = 0
    while word < len(m):
        if m[word] == "#":
            m[word - 1] += "#"
            del m[word]
        else:
            word += 1

    for music in musicinfos:
        arr = music.split(',')
        start, end = arr[0].split(':'), arr[1].split(':')
        start_hour, start_min = int(start[0]), int(start[1])
        end_hour, end_min = int(end[0]), int(end[1])

        hour, min =  end_hour - start_hour, end_min - start_min

        time = hour * 60 + min + 1

        name = arr[2]
        scale = list(str(arr[3]))
        chk = 0
        while chk < len(scale):
            if scale[chk] == "#":
                scale[chk - 1] += "#"
                del scale[chk]
            else:
                chk += 1

        idx = 0
        res = []

        while idx < time:

            res.append(scale[idx % len(scale)])
            idx += 1

        loc = 0
        while loc < len(res) - len(m):
            correct = True
            for c in range(len(m)):
                if res[loc+c] != m[c]:
                    correct = False
                    break
            if correct:

                if answer[1] < time:
                    answer = [name, time, int(start[0]+start[1])]
                    break

            loc += 1

    return answer[0]




a = "ABC"
b = ["11:58,12:14,HELLO,C#DEFGA", "12:50,13:05,WORLD,ACDEF"]
print(solution(a,b))