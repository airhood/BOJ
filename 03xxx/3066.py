def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

T = int(input())

for t in range(T):
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    tail = []

    for j in range(N):
        idx = lower_bound(tail, arr[j])
        if idx == len(tail):
            tail.append(arr[j])
        else:
            tail[idx] = arr[j]
    
    print(len(tail))