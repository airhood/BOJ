N = int(input())

animals = set()
for _ in range(N):
    k, L, R = map(int, input().split())
    animals.add((-L, R))

animals = sorted(animals)

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

for L, R in animals:
    idx = lower_bound(tail, R)
    if idx == len(tail):
        tail.append(R)
    else:
        tail[idx] = R

print(len(tail))