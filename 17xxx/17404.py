INF = 999999999

N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
ans = INF

for c in range(3):
    dp[0][c] = cost[0][c]
    dp[0][(c+1)%3] = dp[0][(c+2)%3] = INF
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    ans = min(ans, min(dp[N-1][(c+1)%3], dp[N-1][(c+2)%3]))
    
print(ans)