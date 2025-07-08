n, m = map(int, input().split())

inp = []
for _ in range(n):
    inp.append(list(map(int, list(input().strip()))))

dp = [[0 for _ in range(m)] for _ in range(n)]
mx = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = inp[i][j]
        elif inp[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        mx = max(mx, dp[i][j])

print(mx**2)