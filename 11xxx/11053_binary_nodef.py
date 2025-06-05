N = int(input())
arr = list(map(int, input().split()))

tail = []

for x in arr:
    left, right = 0, len(tail)
    while left < right:
        mid = (left + right) // 2
        if tail[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    idx = left

    if idx == len(tail):
        tail.append(x)
    else:
        tail[idx] = x

print(len(tail))
