def solution(phone_book):
    dict_phone = {}
    for idx in range(len(phone_book)):
        dict_phone[idx] = phone_book[idx]
    for k, v in dict_phone.items():
        for num in range(len(dict_phone)):
            if len(v) < len(dict_phone[num]):
                if v == dict_phone[num][:len(v)]:
                    return False
    return True

a = ["119", "97674223", "1195524421"]
b = ["12", "123", "1235", "567", "88"]
print(solution(a))
