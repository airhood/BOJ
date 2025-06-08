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

N = int(input())
arr = [int(input()) for _ in range(N)]

up = []
down = []

ans = 0

for i in range(N):
    fix = arr[i]
    up = []
    down = []
    for j in range(i+1, N):
        if fix < arr[j]:
            idx = lower_bound_up(up, arr[j])
            if idx == len(up):
                up.append(arr[j])
            else:
                up[idx] = arr[j]
        if fix > arr[j]:
            idx = lower_bound_down(down, arr[j])
            if idx == len(down):
                down.append(arr[j])
            else:
                down[idx] = arr[j]

    ans = max(ans, len(up) + len(down) + 1) # 기준점까지 포함해서 +1

print(ans)