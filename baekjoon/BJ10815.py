from sys import stdin

N = int(stdin.readline())
card_arr = sorted(list(map(int,stdin.readline().split())))


M = int(stdin.readline())
chk_arr = list(map(int,stdin.readline().split()))

answer = []

for num in chk_arr:
    chk = True
    start, end = 0, len(card_arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if card_arr[mid] == num:
            answer.append("1")
            chk = False
            break
        else:
            if card_arr[mid] > num:
                end = mid - 1
            else:
                start = mid + 1
    if chk:
        answer.append("0")
print(" ".join(answer))