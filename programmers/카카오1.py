def solution(s):
    answer = ''
    num_dict = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    word = ''
    
    for c in s:
        
        if c.isdigit():
            if word:
                answer += str(num_dict[word])
            answer += c
            word = ''
        else:
            word += c
            if word in num_dict:
                answer += str(num_dict[word])
                word = ''



    return int(answer)

a = "one4seveneight"
print(solution(a))