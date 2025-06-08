def lower_bound_up(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def lower_bound_down(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            left = mid + 1
        else:
            right = mid
    return left

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
query = [int(input()) for _ in range(Q)]

len_up = [0] * N
tail_up = []
for i in range(N):
    idx = lower_bound_up(tail_up, arr[i])
    if idx == len(tail_up):
        tail_up.append(arr[i])
    else:
        tail_up[idx] = arr[i]
    
    len_up[i] = idx + 1

len_down = [0] * N
tail_down = []
for i in reversed(range(N)):
    idx = lower_bound_down(tail_down, arr[i])
    if idx == len(tail_down):
        tail_down.append(arr[i])
    else:
        tail_down[idx] = arr[i]

    len_down[i] = idx + 1

for x in query:    
    print(len_up[x-1] + len_down[x-1] - 1)