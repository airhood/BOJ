INF = 100000000

arr = list(map(int, input().split()))
arr.pop()
N = len(arr)
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(N+1)]
arr = [0] + arr

cost = [[1, 2, 2, 2, 2],
        [INF, 1, 3, 4, 3],
        [INF, 3, 1, 3, 4],
        [INF, 4, 3, 1, 3],
        [INF, 3, 4, 3, 1]]
# cost[from][to]

dp[0][0][0] = 0

for i in range(1, N+1):
    # left move
    for r in range(5):
        for l_prev in range(5):
            dp[i][arr[i]][r] = min(dp[i][arr[i]][r], dp[i-1][l_prev][r] + cost[l_prev][arr[i]])
    
    # right move
    for l in range(5):
        for r_prev in range(5):
            dp[i][l][arr[i]] = min(dp[i][l][arr[i]], dp[i-1][l][r_prev] + cost[r_prev][arr[i]])

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[N][l][r])

print(ans)