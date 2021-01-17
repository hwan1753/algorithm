from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))

# 만약 배열 크기가 1이면 1출력하고 종료
if len(arr) == 1:
    print("1")
else:

    answer = 0  # 결과값
    # 모든 인덱스 탐색
    for idx in range(len(arr)):
        # 왼쪽 부분과 오른쪽 부분 나눠서 실행
        # 값 부분은 stack으로 숫자 입력
        left_stack, right_stack = [], []
        
        # 왼쪽 부분
        for i in range(idx):
            # 해당값보다 큰 경우 넘어가기
            if arr[i] >= arr[idx]:
                continue
            # 첫번째 값.
            elif left_stack == []:
                left_stack.append(arr[i])
            else:
                # 만약 stack 마지막 값보다 큰 경우는 추가
                if left_stack[-1] < arr[i]:
                    left_stack.append(arr[i])
                # 만약 stack 마지막 값보다 작은 경우
                # 이분 탐색으로 해당 값이 들어갈 위치 찾아서 교체
                else:
                    left_stack[bisect_left(left_stack, arr[i])] = arr[i]

        # 오른쪽 부분
        for i in range(len(arr) - 1, idx,-1):
            # 해당값보다 큰 경우 넘어가기
            if arr[i] >= arr[idx]:
                continue
            # 첫번째 값
            elif right_stack == []:
                right_stack.append(arr[i])
            else:
                # 만약 stack 마지막 값보다 큰 경우는 추가
                if right_stack[-1] < arr[i]:
                    right_stack.append(arr[i])
                # 만약 stack 마지막 값보다 작은 경우
                # 이분 탐색으로 해당 값이 들어갈 위치 찾아서 교체
                else:
                    right_stack[bisect_left(right_stack, arr[i])] = arr[i]

        # 만약 오른쪽 부분이 있는 경우 해당값 추가
        if right_stack:
            right_stack.append(arr[idx])
        # 없는 경우에는 왼쪽 부분에 해당값 추가
        else:
            left_stack.append(arr[idx])
        # answer와 왼쪽, 오른쪽 배열 갯수 비교하여 큰 값 저장
        answer = max(answer, len(left_stack) + len(right_stack))

    print(answer)