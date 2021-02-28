from itertools import chain

def merge_sort(x, nx):
    if len(x) > 1:
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        nlx, nrx = nx[:mid], nx[mid:]

        lx, nlx = merge_sort(lx, nlx)
        rx, nrx = merge_sort(rx, nrx)


        li, ri, i = 0, 0, 0

        while li < len(lx) and ri < len(rx):
            if int(lx[li]) <= int(rx[ri]):
                x[i] = lx[li]
                nx[i] = nlx[li]
                li += 1
            else:
                x[i] = rx[ri]
                nx[i] = nrx[ri]
                ri += 1
            i += 1
        if li != len(lx):
            x[i:] = lx[li:]
            nx[i:] = nlx[li:]
        else:
            x[i:] = rx[ri:]
            nx[i:] = nrx[ri:]
    return x, nx

def solution(files):
    arr = {}
    for file in files:

        head = ""
        number = ""

        for c in file:
            if not c.isnumeric():
                if number == "":
                    head += c
                else:
                    break
            elif c.isnumeric():
                number += c

        # print(head, number, tail)
        if head.lower() not in arr:
            arr[head.lower()] =[[number], [file]]
        else:
            arr[head.lower()][0].append(number)
            arr[head.lower()][1].append(file)

    # print(arr)

    for a, b in arr.items():
        num, name = merge_sort(b[0],b[1])
        arr[a] = [num, name]

    # print(arr)

    name_arr = sorted(arr)
    answer = []
    for name in name_arr:
        answer.append(arr[name][1])


    return list(chain(*answer))


a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG010.GIF", "img2.JPG", "img1.PNG","img1100.zip","abc1000.zip","bsv11.ziz","iip400.zip", "abc123defg123.jpg"]
b = ["F-50", "B-50 Superfortress", "A-10 Thunderbolt II", "F- 010 Tomcat"]
print(solution(a))