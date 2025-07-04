N = int(input())
arr = list(map(int, input().split()))

x = arr[0]
for i in range(1, N):
    x = x ^ arr[i]

if x == 0:
    print("cubelover")
else:
    print("koosaga")