def solution(n, words):

    word_dict = {}
    idx = 0
    count = 0
    last_word = words[0][0]

    while True:


        if idx == len(words):
            return [0,0]
        if words[idx] not in word_dict and words[idx][0] == last_word:
            word_dict[words[idx]] = 1
            last_word = words[idx][-1]
            idx += 1


            if idx % n == 0:

                count += 1
        else:
            count += 1
            if (idx+1) % n:
                return [(idx+1) % n, count]
            else:
                return [n, count]



a = 2
b = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(a,b))