def solution(n, k, cmd):
    answer = ''
    arr = ['O']*(n)
    
    stack = []
    count_z = 0
    for cc in range(len(cmd)-1,-1,-1):
        if cmd[cc].split()[0] == 'Z':
            count_z += 1
        elif cmd[cc].split()[0] == 'C' and count_z > 0:
            cmd[cc] = ["D 1", "U 1"]


    for cc in cmd:
        input_ = cc.split()
        if input_[0] == 'D':
            for i in range(int(input_[1])):
                if k < n-1:
                    k+=1
                    while arr[k] == 'X':
                        k+=1
        
        elif input_[0] == 'U':
            for i in range(int(input_[1])):
                if k >0:
                    k -= 1
                    while arr[k] == 'X':
                        k-=1
        
        elif input_[0] == 'C':
            arr[k] = 'X'
            stack.append(k)
            if k == n-1:
                while arr[k] == 'X':
                    k-=1
            elif arr[k:].count('O') == 0:
                while arr[k] == 'X':
                    k-=1
            else:
                while arr[k] == 'X':
                    k+=1
        elif input_[0] == 'Z':
            if stack:
                arr[stack.pop()] = 'O'
        # print(arr)
    return "".join(arr)

a1 = 8
a2 = 2
a3 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(a1,a2,a3))