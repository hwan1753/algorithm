def contest1(rank):
    global money
    if rank == 1:
        money += 5000000
    elif rank <= 3:
        money += 3000000
    elif rank <= 6:
        money += 2000000
    elif rank <= 10:
        money += 500000
    elif rank <= 15:
        money += 300000
    elif rank <= 21:
        money += 100000
    else:
        money += 0

def contest2(rank):
    global money
    if rank == 1:
        money += 5120000
    elif rank <= 3:
        money += 2560000
    elif rank <= 7:
        money += 1280000
    elif rank <= 15:
        money += 640000
    elif rank <= 31:
        money += 320000
    else:
        money += 0

money = 0
result = []
count = input()
# if count > 0 and count <= 1000:
for num in range(int(count)):
    a = input()
    b = a.split(' ')
    contest1(int(b[0]))
    contest2(int(b[1]))
    result.append(money)
    money = 0
for pp in result:
    print(pp)
