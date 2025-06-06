N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1_idx = [-1] * (N + 1)

for i in range(N):
    arr1_idx[arr1[i]] = i

arr = []

for i in range(N):
    arr.append(arr1_idx[arr2[i]])

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

for x in arr:
    idx = lower_bound(tail, x)
    if idx == len(tail):
        tail.append(x)
    else:
        tail[idx] = x

print(len(tail))