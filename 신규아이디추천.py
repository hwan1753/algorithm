import re

def solution(new_id):
    change_id = new_id
    # 1 단계
    change_id = change_id.lower()
    # 2 단계
    change_id = re.findall(r'[a-zA-Z0-9\-_.]',change_id)
    next_id = ""
    for i in change_id:
        next_id += i
    change_id = next_id
    # print(change_id,2)
    # 3 단계
    change_id = re.sub(r"\.+",'.',change_id)
    # print(change_id,3)
    # 4 단계
    if change_id:
        if change_id[0] == '.':
            change_id = change_id[1:]
    if change_id:
        if change_id[-1] == '.':
            change_id = change_id[:-1]
    # print(change_id,4)
    # 5 단계
    if change_id == '':
        change_id = 'a'
    # print(change_id, 5)
    # 6 단계
    if len(change_id) >= 16:
        change_id = change_id[:15]
        if change_id[-1] == '.':
            change_id = change_id[:-1]
    # print(change_id, 6)
    if len(change_id) < 3:
        while len(change_id) < 3:
            change_id += change_id[-1]
    return change_id

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


a = "...!@BaT#*..y.abcdefghijklm"
print(solution(a))
b = "z-+.^."
print((solution(b)))
c = "=.="
print(solution(c))
d = "123_.def"
print(solution(d))
e = "abcdefghijklmn.p"
print(solution(e))