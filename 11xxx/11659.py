N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    if i == 0:
        print(arr[j])
    else:
        print(arr[j] - arr[i-1])