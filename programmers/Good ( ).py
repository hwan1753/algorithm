def solution(s):
    answer = True
    arr = list(str(s))
    chk = 0
    for x in arr:
        if x == "(":
            chk += 1
        else:
            chk -= 1
        if chk < 0:
            return False
    if chk != 0:
        return False

    return True

a = "()()"
print(solution(a))