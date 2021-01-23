from sys import stdin

def find_queen(sol, n):
    global answer

    if len(sol) == N:
        answer += 1
        return  0

    candidate = [i for i in range(n)]
    for i in range(len(sol)):
        distance = len(sol) - i
        if sol[i] in candidate:
            candidate.remove(sol[i])

        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)

        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)

    if candidate != []:
        for i in candidate:
            find_queen(sol + [i], n)
    else:
        return 0


N = int(stdin.readline())
answer = 0

for i in range(N):
    find_queen([i], N)
print(answer)