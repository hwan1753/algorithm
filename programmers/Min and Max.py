def solution(s):
    arr = s.split()
    for num in range(len(arr)):
        arr[num] = int(arr[num])
    # print(max(arr), min(arr))

    return str(min(arr)) + " " + str(max(arr))

a = "1 2 3 4"
solution(a)
b = "-1 -2 -3 -4"
solution(b)