from sys import stdin

for t in range(int(stdin.readline())):
    K = int(stdin.readline())
    N = int(stdin.readline())

    matrix = [[0] * (N+1) for _ in range(K+1)]
    matrix[0] = [i for i in range(N+1)]
    # print(matrix)

    for k in range(1, K+1):
        for n in range(1, N+1):
            matrix[k][n] = matrix[k-1][n] + matrix[k][n-1]
    print(matrix[K][N])