from sys import stdin

def kmpSearch(H, N):
    n = len(H)
    m = len(N)

    # 결과값 리스트
    ret = []
    # pi[i]는 N[~i]의 접두사도 되고 접미사도 되는 문자열의 최대길이
    pi = getPartialMatch(N)

    begin = 0
    matched = 0
    while begin <=n - m:
        # 글자가 일치한다면
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            # m글자가 모두 일치한다면
            if matched == m:
                ret.append(begin)

        else:
            # matched가 0인 경우 다음 칸에서 시작
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched -1]
    return ret

def getPartialMatch(N):
    m = len(N)
    pi = [0] * m

    # KMP로 N에서 N을 찾는다(begin은 1부터)
    begin = 1
    matched = 0
    # 비교할 문자가 N의 끝에 도달할 때까지 부분 일치를 모두 기록
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


str_arr = list(stdin.readline().rstrip())
find_str = list(stdin.readline().rstrip())
x = kmpSearch(str_arr, find_str)
print(len(x))
for i in x:
    print(i+1, end=' ')

