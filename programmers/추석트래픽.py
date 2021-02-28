def solution(lines):
    queue = []
    max = 0
    for li in lines:
        array = list(map(str,li.split()))
        date, time, do = array[0], array[1], array[2]
        hh, mm, ss = map(str, time.split(':'))
        h, m = int(hh), int(mm)
        s_0, s_1 = map(int, ss.split('.'))
        if do[1] == '.':
            do_0, do_1 = map(str,do.split('.'))
            d_0 = int(do_0)
            d_1 = int(do_1[:len(do_1)-1])
        else:
            d_0 = int(do[0])
            d_1 = 0
        print(d_0, d_1)
        after = h * (10 ** 7) + m * (10 ** 5) + s_0 * (10 ** 3) + s_1
        if s_0 - d_0 < 0:
            if m == 0:
                h = h - 1
                m = 59
            else:
                m = m - 1
            s_0 = s_0 - d_0 + 60
        else:
            s_0 = s_0 - d_0


        if s_1 - d_1 < 0:
            if s_0 == 0:
                if m == 0:
                    h = h -1
                    m = 59
                else:
                    m = m -1
                s_0 = 59

            else:
                s_0 = s_0 -1
            s_1 = s_1 - d_1 + 1000 + 1
        else:
            s_1 = s_1 - d_1 + 1
        before = h * (10 ** 7) + m * (10 ** 5) + s_0 * (10 ** 3) + s_1
        queue.append([before,after])
    # print(queue)

    for idx in queue:

        start = idx[1]
        end = idx[1] + 1000
        res = 0
        for chk in queue:
            # print(chk)
            if start >= chk[0] and end <= chk[1]:
                res += 1
                # print('res')
            elif start <= chk[1] < end:
                res += 1
                # print('res2')
            elif start <= chk[0] < end:
                res += 1
                # print('res3')
            if res > max:
                max = res
    #     print(res)
    # print("max : {}".format(max))
    return max

a = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
b= ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
solution(b)