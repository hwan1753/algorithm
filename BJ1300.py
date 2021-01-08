from sys import stdin

# Input 값
N = int(stdin.readline())
K = int(stdin.readline())

# 이분탐색 시작값과 마지막 값.
start, end = 1, N ** 2
answer = 0  # 정답값

# 이분탐색 실행.
while start <= end:
    middle = (start + end) // 2
    count = 0
    # 해당 값이 N이상으로 나눠지는지, N개인지, 그보다 적은지 판단
    # middle보다 작은 값 갯수 카운팅
    for i in range(1, N+1):
        count += min(middle//i, N)

    # 만약 갯수가 K보다 많거나 작으면 end값 땡겨서 범위 축소
    if count >= K:
        end = middle - 1
        answer = middle
    # 만약 갯수가 K보다 적으면 start값 땡겨서 범위 축소
    else:
        start = middle + 1
print(answer)
print(start)