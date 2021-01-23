from sys import stdin

def find_queen(sol, n):
    global answer

    # sol 갯수가 N개가 되면 + 1
    if len(sol) == N:
        answer += 1
        return  0
    # 후보자 리스트.
    candidate = [i for i in range(n)]
    for i in range(len(sol)):
        # sol의 i번째와 현재 열의 거리.
        distance = len(sol) - i
        # 같은 열의 후보 제거
        if sol[i] in candidate:
            candidate.remove(sol[i])
        # 해당 퀸의 대각선의 +방향 확인
        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)
        # 해당 퀸의 대각선의 -방향 확인
        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)
    
    if candidate != []:
        for i in candidate:
            # 후보를 추가하여 재귀 실행
            find_queen(sol + [i], n)
    # 후보가 없는경우 종료
    else:
        return 0


N = int(stdin.readline())
answer = 0

for i in range(N):
    find_queen([i], N)
print(answer)