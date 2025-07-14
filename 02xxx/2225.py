N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)] # i를 j개의 합으로 표현하는 경우의 수

MOD = 10**9

for i in range(K+1):
    dp[0][i] = 1

for i in range(1, N+1):
    for j in range(1, K+1):
        for k in range(i+1):
            dp[i][j] += dp[i-k][j-1]
            dp[i][j] %= MOD

print(dp[N][K])