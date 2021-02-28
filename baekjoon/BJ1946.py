import sys

T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    chk = []
    for n in range(N):
        a = list(map(int,input().split()))
        arr.append(a)

    arr.sort()

    cnt = 0
    aMax = 100001
    bMax = 100001
    for i in arr:
        if i[0] < aMax and i[1] > bMax:
            cnt += 1
            aMax = i[0]
        elif i[0] > aMax and i[1] < bMax:
            cnt += 1
            bMax = i[1]
        elif i[0] < aMax and i[1] < bMax:
            cnt += 1
            aMax = i[0]
            bMax = i[1]
    print(cnt)

    # for idx in range(len(value)):
    #     add = True
    #
    #     cc = 0
    #     while cc <len(chk):
    #         if i[0] > chk[cc][0] and i[1] > chk[cc][1]:
    #             add = False
    #             break
    #         elif i[0] < chk[cc][0] and i[1] < chk[cc][1]:
    #             del chk[cc]
    #         else:
    #             cc += 1
    #     if add == True:
    #         chk.append(i)

    # print(len(chk))