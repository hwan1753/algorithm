def solution(s):

    change_transform = 0
    remove_zero = 0
    sentence = s

    while len(sentence) > 2:

        new_sentence = ""
        chk_one = sentence.count("1")
        remove_zero += sentence.count("0")
        len_next = chk_one

        while len_next > 1:

            new_sentence = str(len_next % 2) + new_sentence
            len_next = len_next // 2

        if chk_one != 2 and chk_one != 3:
            new_sentence = "1" + new_sentence
            change_transform += 1
        elif chk_one == 3:
            change_transform += 3
            remove_zero += 1
            return [change_transform, remove_zero]
        else:
            change_transform += 2
            remove_zero += 1
            return [change_transform, remove_zero]

        sentence = new_sentence

    return [change_transform, remove_zero]





s1 = "11001010100111"
print(solution(s1))
s2 = "01110"
# print(solution(s2))
s3 = "1111111"
