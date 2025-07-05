T = int(input())

coins = [1, 10, 25]

for _ in range(T):
    t = int(input())
    dp = [1 << 15] * 100
    dp[0] = 0
    answer = 0
    for c in coins:
        for i in range(c, 100):
            dp[i] = min(dp[i], dp[i-c] + 1)
    while t > 0:
        answer += dp[t % 100]
        t //= 100
    print(answer)