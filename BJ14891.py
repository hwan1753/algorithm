from _collections import deque

gear = [0]
for num in range(4):
    gear.append(deque(list(map(int,input()))))

K = int(input())
for num in range(K):
    idx, direction = map(int, input().split())

    up_chk = gear[idx][2]
    down_chk = gear[idx][6]

    if direction == 1:
        gear[idx].appendleft(gear[idx].pop())
    else:
        gear[idx].append(gear[idx].popleft())
    # print(gear[idx])

    up, down = idx + 1, idx - 1
    up_direction, down_direction = direction, direction

    while up < 5:
        if gear[up][6] != up_chk:
            if up_direction == 1:
                up_chk = gear[up][2]
                gear[up].append(gear[up].popleft())
                up_direction = -1
            else:
                up_chk = gear[up][2]
                gear[up].appendleft(gear[up].pop())
                up_direction = 1
            # print(up, gear[up])
            up += 1

        else:
            break

    while down > 0:
        if gear[down][2] != down_chk:
            if down_direction == 1:
                down_chk = gear[down][6]
                gear[down].append(gear[down].popleft())
                down_direction = -1
            else:
                down_chk = gear[down][6]
                gear[down].appendleft(gear[down].pop())
                down_direction = 1
            # print(down, gear[down])
            down -= 1
        else:
            break
# print(gear)
answer = 0
score = 1
for num in range(1,5):
    if gear[num][0] == 1:
        answer += score
    score *= 2
print(answer)