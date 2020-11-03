def solution(key, lock):
    answer = True

    key_value = []
    lock_hom = []

    for a in range(len(key)):
        for b in range(len(key)):
            if key[a][b] == 1:
                key_value.append([a,b])

    for y in range(len(lock)):
        for x in range(len(lock)):
            if lock[y][x] == 0:
                lock_hom.append([y,x])
    print(key_value)
    print(lock_hom)



    return answer

a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
b = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(a,b)