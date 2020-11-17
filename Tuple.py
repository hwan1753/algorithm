from itertools import chain

def solution(s):
    answer = []
    arr = []
    len_arr = []
    k = []
    tmp = ""
    idx = 0
    for i in s:

        if i.isnumeric():
            tmp += i
        elif i == "," and tmp != "":
            k.append(int(tmp))
            tmp = ""
        elif i == "}"and tmp != "":
            k.append(int(tmp))
            arr.append([len(k),k])
            len_arr.append([len(k),idx])
            tmp = ""
            k = []
            idx += 1

    # print(sorted(arr))
    for x in sorted(arr):
        answer.append(x[1])
    answer = list(chain(*answer))

    res = []
    for x in answer:
        if x not in res:
            res.append(x)

    return res

a = "{{20,111},{111}}"
print(solution(a))
