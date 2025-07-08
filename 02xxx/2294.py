INF = 999999

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [INF] * (k+1)
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i-c]+1, dp[i])

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])