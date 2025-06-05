def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

N = int(input())
arr = list(map(int, input().split()))

tail = []

for x in arr:
    idx = lower_bound(tail, x)
    if idx == len(tail):
        tail.append(x)
    else:
        tail[idx] = x

print(len(tail))
