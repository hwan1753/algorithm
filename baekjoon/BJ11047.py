T = list(map(int,input().split()))
X = []
for cnt in range(T[0]):
    X.append(int(input()))

value = T[1]
idx = len(X) - 1
result = 0
while value != 0:
    result += value // X[idx]
    value = value % X[idx]
    idx -= 1
print(result)