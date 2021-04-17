from sys import stdin
from itertools import chain

input_ = stdin.readline().rstrip()
bomb = list(stdin.readline().rstrip())
temp = []
chk_start = bomb[-1]

for i in input_:

    temp += [i]
    if len(temp) < len(bomb):
        continue
    
    if i == chk_start and temp[len(bomb)*-1:] == bomb:
        # temp = temp[:len(bomb)*-1]
        for i in range(len(bomb)):
            temp.pop()

if temp:
    print("".join(temp))
else:
    print("FRULA")