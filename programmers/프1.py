def solution(code, day, data):
    answer = []
    temp = []
    for d in data:
        p, c, t = d.split(' ')
        
        if c.split('=')[1] == code and t.split('=')[1][:-2] == day:
            temp.append((t.split('=')[1][-2:],int(p.split('=')[1])))

    temp.sort()
    answer = [i for _, i in temp]
    return answer

a = "012345"	
b = "20190620"	
c = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]	
print(solution(a,b,c))