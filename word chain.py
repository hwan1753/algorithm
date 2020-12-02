def solution(n, words):

    word_dict = {}  # 이전에 나온 단어인지 확인용 dictionary
    idx = 0         # 번호 순서 확인 변수
    count = 1       # 사람이 몇 번째 단어가 틀렸는지 확인 변수
    last_word = words[0][0] # 처음 시작 단어 첫 글자

    while True:

        if idx == len(words):   # 만약 모든 단어를 진행했다면 틀린 사람 없음
            return [0,0]
        if words[idx] not in word_dict and words[idx][0] == last_word:  # 단어가 이전에 안나왔고 앞 단어의 마지막 글자와 일치
            word_dict[words[idx]] = 1   # dictionary에 추가
            last_word = words[idx][-1]  # 마지막 글자 저장
            idx += 1

            if idx % n == 0:    # 만약 n번째 사람이 대답 했다면 단어 + 1
                count += 1
        else:
            if (idx+1) % n:     # 만약 n번째가 아니면 n으로 나눈 나머지 번째 사람
                return [(idx+1) % n, count]
            else:               # n 번째 사람.
                return [n, count]



a = 2
b = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(a,b))