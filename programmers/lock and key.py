def rotation(arr):
    size = len(arr)
    temp_arr = [[0] * len(arr) for _ in range(len(arr))]
    for y in range(size):
        for x in range(size):
            temp_arr[x][size - y - 1] = arr[y][x]
    return temp_arr

def padding(size, my, mx, key):
    temp_arr = [[0] * size for _ in range(size)]
    for y in range(len(key)):
        for x in range(len(key)):
            temp_arr[y + my][x + mx] = key[y][x]
    for i in temp_arr:
        print(i)
    print("!"*10)
    return temp_arr

def chk_key(key, lock, a ,b):

    for y in range(a, a + b):
        for x in range(a, a + b):
            # if lock[y][x] == 2:
            #     continue
            if lock[y][x] + key[y][x] == 2 or lock[y][x] + key[y][x] == 0:
                return False
    return True

def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    key_matrix = [[2] * (lock_size + 2 * key_size - 2) for _ in range(lock_size + 2 * key_size - 2)]


    for y in range(lock_size):
        for x in range(lock_size):
            key_matrix[y + key_size - 1][x + key_size - 1] = lock[y][x]

    for _ in key_matrix:
        print(_)

    for _ in range(4):
        for my in range(len(key_matrix) - key_size+1):
            for mx in range(len(key_matrix) - key_size+1):

                temp_key = padding(len(key_matrix), my, mx, key)
                answer = chk_key(temp_key,key_matrix, key_size - 1, lock_size)

                if answer:
                    return answer

        key = rotation(key)
    return False


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],[1, 0, 1, 0]]
print(solution(a,b))