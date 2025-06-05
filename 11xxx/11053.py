N = int(input())
list = list(map(int, input().split()))

dp = [0] * 1000

for element in list:
    prev_max = 0
    for j in range(0, element - 1):
        prev_max = max(prev_max, dp[j])
    dp[element - 1] = prev_max + 1

max_count = 0
for element in dp:
    max_count = max(max_count, element)

print(max_count)