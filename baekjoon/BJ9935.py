from sys import stdin
from itertools import chain

# input_ = list(map(str, stdin.readline()))
# bomb = list(map(str,stdin.readline()))

input_ = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
temp = input_

while True:

    before = temp
    a = temp.split(bomb)
    
    chk = ''
    for i in a:
        chk += i
    if before == chk:
        if before == '':
            print('FRULA')
        else:
            print(before)
        break
    else:
        temp = chk
    
    
