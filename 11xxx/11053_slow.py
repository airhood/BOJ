N = int(input())
list = list(map(int, input().split()))

dp = [0] * N

for i in range(0, N):
    if dp[i] == 0:
        dp[i] = 1
    for j in range(0, i):
        if list[i] > list[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

max_count = 0
for element in dp:
    max_count = max(max_count, element)

print(max_count)