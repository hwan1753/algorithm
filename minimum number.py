def solution(A,B):
    answer = 0
    
    A = sorted(A)   # 오름차순으로 정렬
    B = list(reversed(sorted(B)))   #  내림차순으로 정렬
    
    # index 별로 곱하여 더하기
    for idx in range(len(A)):
        answer += A[idx] * B[idx]

    return answer

a = [1, 4, 2]
b = [1, 2, 4]
print(solution(a,b))