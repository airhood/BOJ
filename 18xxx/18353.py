def upper_bound_dec(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            left = mid + 1
        else:
            right = mid
    return right

N = int(input())
arr = list(map(int, input().split()))

tail = []

for x in arr:
    idx = upper_bound_dec(tail, x)
    if idx == len(tail):
        tail.append(x)
    else:
        tail[idx] = x

print(N - len(tail))