def solution(s):

    change_transform = 0
    remove_zero = 0
    sentence = s

    while len(sentence) > 2:

        new_sentence = ""
        chk_one = sentence.count("1")
        remove_zero += sentence.count("0")
        len_next = chk_one
        # print("len_next{}".format(chk_one))
        while len_next > 2:

            new_sentence = str(len_next % 2) + new_sentence
            len_next = len_next // 2
            # print(len_next)
        new_sentence = "1" + new_sentence
        sentence = new_sentence
        change_transform += 1
        print(remove_zero)
        print(change_transform)
        print(sentence)


    if sentence == "11":
        change_transform += 2
        remove_zero += 1

    elif sentence == "01":
        change_transform += 1
        remove_zero += 1

    elif sentence == "1":
        change_transform += 1


    return [change_transform, remove_zero]

s1 = "110010101001"
print(solution(s1))
s2 = "01110"
# print(solution(s2))
s3 = "1111111"
