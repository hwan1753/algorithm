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
    # 3 단계
    change_id = re.sub(r"\.+",'.',change_id)
    # 4 단계
    if change_id:
        if change_id[0] == '.':
            change_id = change_id[1:]
    if change_id:
        if change_id[-1] == '.':
            change_id = change_id[:-1]
    # 5 단계
    if change_id == '':
        change_id = 'a'
    # 6 단계
    if len(change_id) >= 16:
        change_id = change_id[:15]
        if change_id[-1] == '.':
            change_id = change_id[:-1]
    if len(change_id) < 3:
        while len(change_id) < 3:
            change_id += change_id[-1]
    return change_id

def solution(new_id):
    st = new_id
    # 1단계
    # lower로 대문자 -> 소문자
    st = st.lower()

    # 2단계
    # ^은 not을 의미, [a-z, 0-9, -, _, .] 을 제외한 나머지 ''로 바꾸기
    st = re.sub('[^a-z0-9\-_.]', '', st)

    # 3단계
    # .이 1번 이상 반복되는 모든 글자를 '.'로 바꾸기
    # 여기서 \.+ 에서 \는 욕심없는 반복으로 변형, .이 있는 글자만 포함
    st = re.sub('\.+', '.', st)
    # \를 제외하면 .뒤의 모든 글자를 1개로 처리함.
    # st = re.sub('.+', '.', st)
    # +는 {1,}로 바꿀 수 있음. .{1,}는 .이 1번이상 반복되는 글자를 그룹화하는 것을 의미함.
    # st = re.sub('\.{1,}','.',st)

    # 4단계
    # ^[.]은 문자열 시작이 .로 시작하는 것을 의미
    # |은 or을 의미
    # [.]$sms 문자열 끝이 .로 끝나는 것을 의미
    st = re.sub('^[.]|[.]$', '', st)

    # 5단계, 6단계
    # 만약 0글자이면 'a'
    # 아니면 15까지, st가 15보다 작다면 끝까지 포함하기 때문에 :15까지 슬라이싱해도 끝까지 하는 것과 같음.
    st = 'a' if len(st) == 0 else st[:15]

    # 4단계 반복
    st = re.sub('^[.]|[.]$', '', st)

    # 7단계
    # 길이가 3보다 작다면 마지막 글자( == [-1])를 3 - len(st)만큼 반복해서 st에 붙임.
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


a = "...-!@BaT#*..y.abcdefghijklm"
print(solution(a))
# b = "z-+.^."
# print((solution(b)))
# c = "=.="
# print(solution(c))
# d = "123_.def"
# print(solution(d))
# e = "abcdefghijklmn.p"
# print(solution(e))