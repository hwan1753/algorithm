from sys import stdin

def kmp(H, N):
    n = len(H)
    m = len(N)

    ret = []

    pi = getPartialMatch(N)
    # print(pi)
    begin = 0
    match = 0

    while begin <= n-m:
         
        if match < m and H[begin + match] == N[match]:
            match += 1
            
            if match == m:
                ret.append(begin)

        else:
            
            if match == 0:
                begin += 1
            else:
                begin += match - pi[match - 1]
                match = pi[match -1]
    # print(ret)
    return ret


def getPartialMatch(N):
    m = len(N)
    pi = [0] * m

    begin = 1
    match = 0
    while begin + match < m:
        if N[begin+match] == N[match]:
            match += 1
            pi[begin + match - 1] = match
        else:
            if match == 0:
                begin += 1

            else:
                begin += match - pi[match - 1]
                match = pi[match - 1]
    return pi

            


T = list(stdin.readline().rstrip())
P = list(stdin.readline().rstrip())
x = kmp(T,P)
print(len(x))
for i in x:
    print(i+1, end=' ')
