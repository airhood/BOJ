arr = [list(map(int, input().split())) for _ in range(3)]

sums = []
for i in range(3):
    sums.append(arr[i])
    sums.append([arr[0][i], arr[1][i], arr[2][i]])
sums.append([arr[0][0], arr[1][1], arr[2][2]])
sums.append([arr[0][2], arr[1][1], arr[2][0]])

sum_list = [0, 0, 0]
for s in sums:
    if s.count(0) == 0:
        sum_list = s
        break
    elif s.count(0) < sum_list.count(0):
        sum_list = s

if sum_list.count(0) != 0:
    sum_val = (sum(arr[0]) + sum(arr[1]) + sum(arr[2])) // 2
else:
    sum_val = sum(sum_list)

def switch(arr):
    arr2 = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            arr2[j][i] = arr[i][j]
    return arr2

while True:
    for i in range(3):
        if arr[i].count(0) == 1:
            arr[i][arr[i].index(0)] = sum_val - sum(arr[i])
    arr = switch(arr)
    for i in range(3):
        if arr[i].count(0) == 1:
            arr[i][arr[i].index(0)] = sum_val - sum(arr[i])
    arr = switch(arr)

    for k in range(3):
        if arr[k].count(0) != 0:
            continue
    break

for i in range(3):
    for j in range(3):
        print(arr[i][j], end=' ')
    print('')