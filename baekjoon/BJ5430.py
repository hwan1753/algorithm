from sys import stdin

T = int(stdin.readline())
for test in range(T):
    command = input()
    command_arr = list(str(command.replace('RR','')))
    number = int(input())
    num_list = input()[1:-1].split(',')
    if number == 0 and "D" in command:
        print("error")
        continue
    elif number == 0:
        print("[]")
        continue

    front = 0


    chk =True
    tmp = False
    for ac in command_arr:

        if ac == "R":
            tmp = not tmp
        else:
            if len(num_list) == front:
                chk = False
            elif tmp:
                num_list.pop()
            else:
                front += 1

    if chk:
        if tmp:
            num_list = list(reversed(num_list[front:]))
        else:
            num_list = num_list[front:]
        print("[", end="")
        print(",".join(num_list), end="")
        print("]")
    else:
        print("error")