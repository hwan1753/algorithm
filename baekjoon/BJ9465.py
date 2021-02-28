from sys import stdin

T = int(stdin.readline())

for tc in range(T):
    n = int(stdin.readline())
    
    list_a = list(map(int, stdin.readline().split()))
    list_b = list(map(int, stdin.readline().split()))

    answer = 0
    max_val = -1

    while True:
        
        max_a = max(list_a)
        max_b = max(list_b)
        
        if max_a == 0 and max_b == 0:
            break

        elif max_a >= max_b:
            idx = list_a.index(max_a)
            answer += max_a
            if idx == 0:
                list_a[idx:idx+2] = [0,0]
            elif idx == n-1:
                list_a[idx-1:idx+1] = [0,0]
            else:
                list_a[idx-1:idx+2] = [0,0,0]
            
            list_b[idx] = 0

        else:
            idx = list_b.index(max_b)
            answer += max_b
            if idx == 0:
                list_b[idx:idx+2] = [0,0]
            elif idx == n-1:
                list_b[idx-1:idx+1] = [0,0]
            else:
                list_b[idx-1:idx+2] = [0,0,0]
            list_a[idx] = 0
        
    print(answer)
    
