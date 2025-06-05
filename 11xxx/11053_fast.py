N = int(input())
list = list(map(int, input().split()))

sorted = sorted(list)

key_map = dict()
key_map[sorted[0]] = 0
key_count = 1
for i in range(1, N):
    if sorted[i] != sorted[i - 1]:
        key_map[sorted[i]] = key_count
        key_count += 1

dp = [0] * key_count

for element in list:
    prev_max = 0
    for j in range(0, key_map[element]):
        prev_max = max(prev_max, dp[j])
    dp[key_map[element]] = prev_max + 1

max_count = 0
for element in dp:
    max_count = max(max_count, element)

print(max_count)