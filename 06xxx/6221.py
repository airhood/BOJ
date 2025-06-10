N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

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

for x, y in arr:
    idx = lower_bound(tail, y)
    if idx == len(tail):
        tail.append(y)
    else:
        tail[idx] = y

print(len(tail))