N = int(input())

arr = set()
for _ in range(N):
    L, R = map(int, input().split())
    arr.add((-L, R))

arr = sorted(arr)

def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

tail = []
tail_idx = []
prev_idx = [-1] * N

i = 0
for L, R in arr:
    idx = lower_bound(tail, R)
    if idx == len(tail):
        tail.append(R)
        tail_idx.append(i)
    else:
        tail[idx] = R
        tail_idx[idx] = i

    if idx != 0:
        prev_idx[i] = tail_idx[idx - 1]
    
    i += 1

lis = []

track = tail_idx[-1]
while track != -1:
    lis.append(arr[track])
    track = prev_idx[track]

print(len(lis))
for L, R in lis:
    print(f"{-L} {R}")