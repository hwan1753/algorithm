from sys import stdin

# N 개의 줄
N = int(stdin.readline())

# 배열 RGB값 n개
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 초기 설정값
answer = 1e9

# 1번쨰 줄부터 시작
for n in range(1,N):
    for i in range(3):
        # 미니멈 초기값
        minimum = 1e9
        for j in range(3):
            # 이전과 같은 색인 경우 제외
            # 가장 작은 값 찾기
            if i != j and arr[n][i] + arr[n-1][j] < minimum:
                minimum = arr[n][i] + arr[n-1][j]
        # 가장 작은 값 기록
        arr[n][i] = minimum

print(min(arr[-1]))