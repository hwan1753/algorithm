def solution(s):

    change_transform = 0    # 변환 횟수
    remove_zero = 0         # 0 제거 횟수
    sentence = s            # input 값. 알고리즘 활용 문자

    # 2진수가 3자리 이상인 경우에 반복문 진행.
    while len(sentence) > 2:

        new_sentence = ""   # 변환한 문자
        chk_one = sentence.count("1")   # 1의 갯수, 다음 계산하는 이진수
        remove_zero += sentence.count("0")  # 제거한 0을 더해줌.
        len_next = chk_one  # 1의 갯수, 아래 while문에서 활용하는 변수

        # 1의 갯수를 다시 2진수로 변환. 
        while len_next > 1:

            new_sentence = str(len_next % 2) + new_sentence
            len_next = len_next // 2
        
        # 2진수가 3자리 이상인 경우 1을 추가.
        if chk_one != 2 and chk_one != 3:
            new_sentence = "1" + new_sentence
            change_transform += 1
        
        # 2진수가 "11" 인 경우 3번 변환과 0을 한번 제거
        elif chk_one == 3:
            change_transform += 3
            remove_zero += 1
            return [change_transform, remove_zero]
        
        # 2진수가 "10"인 경우 2번 변환과 0을 한번 제거
        else:
            change_transform += 2
            remove_zero += 1
            return [change_transform, remove_zero]

        sentence = new_sentence
    # 2진수가 "1"로 끝난 경우
    return [change_transform, remove_zero]





s1 = "11001010100111"
print(solution(s1))
s2 = "01110"
# print(solution(s2))
s3 = "1111111"
