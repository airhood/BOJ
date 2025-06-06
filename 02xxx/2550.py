N = int(input())
switch = list(map(int, input().split()))
switch_idx = [0] * 10001

for i in range(N):
    switch_idx[switch[i]] = i

bulb = list(map(int, input().split()))

arr = []

for i in range(N):
    arr.append(switch_idx[bulb[i]])

def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

tail = []
tail_idx = []
prev_idx = [-1] * N

for i in range(N):
    idx = lower_bound(tail, arr[i])

    if idx == len(tail):
        tail.append(arr[i])
        tail_idx.append(i)
    else:
        tail[idx] = arr[i]
        tail_idx[idx] = i

    if idx != 0:
        prev_idx[i] = tail_idx[idx - 1]

lis = []

track = tail_idx[-1]
while track != -1:
    lis.append(arr[track])
    track = prev_idx[track]

lis.reverse()

ans = []

for element in lis:
    ans.append(switch[element])

ans.sort()

print(len(lis))
for element in ans:
    print(f"{element}", end=' ')