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

for i in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    tail = []

    for x in arr:
        idx = lower_bound(tail, x)
        if idx == len(tail):
            tail.append(x)
        else:
            tail[idx] = x
    
    print(f"Case #{i + 1}")
    if len(tail) >= K: print(1)
    else: print(0)