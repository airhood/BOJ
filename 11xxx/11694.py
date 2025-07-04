N = int(input())
arr = list(map(int, input().split()))

one_count = 0

x = arr[0]
if arr[0] == 1:
    one_count += 1
for i in range(1, N):
    if arr[i] == 1:
        one_count += 1
    x = x ^ arr[i]

if one_count == 0:
    if x == 0:
        print("cubelover")
    else:
        print("koosaga")
elif one_count == N:
    if one_count % 2 == 1:
        print("cubelover")
    else:
        print("koosaga")
elif one_count % 2 == 1:
    if x == 0:
        print("cubelover")
    else:
        print("koosaga")
else:
    for i in range(N):
        if arr[i] != 1:
            arr[i] = i
            break

    x = arr[0]
    for i in range(1, N):
        if arr[i] == 1:
            one_count += 1
        x = x ^ arr[i]

    if x == 0:
        print("cubelover")
    else:
        print("koosaga")
