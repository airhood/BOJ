N = int(input())
arr = list(map(int, input().split()))
arr.sort()

INF = 1000000000000000

min_val = INF
result_A = 0
result_B = 0
result_C = 0

for i in range(N):
    left = 0
    right = N-1

    if i == 0:
        left += 1
    if i == N-1:
        right -= 1

    while left < right:
        current = arr[left] + arr[right] + arr[i]
        current_abs = abs(current)
        if (min_val >= current_abs):
            min_val = current_abs
            result_A = arr[left]
            result_B = arr[right]
            result_C = arr[i]

        if current < 0:
            left += 1
            if left == i:
                left += 1
        elif current > 0:
            right -= 1
            if right == i:
                right -= 1
        else:
            break

ans = [result_A, result_B, result_C]
ans.sort()

print(f"{ans[0]} {ans[1]} {ans[2]}")