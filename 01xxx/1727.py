n, m = map(int, input().split())

man = list(map(int, input().split()))
women = list(map(int, input().split()))

man.sort()
women.sort()

dp = [[0 for _ in range(m)] for _ in range(n)]
# dp[i][j] -> 0 ~ i 까지의 man과 0 ~ j 까지의 women 을 고려하였을 때의 성격의 차이의 핪의 최솟값
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(man[i] - women[j]))   .....  i > j  (일부 남자가 솔로)
# dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(man[i] - women[j]))   .....  j > i  (일부 여자가 솔로)
# dp[i][j] = dp[i-1][j-1] + abs(man[i] - women[j])                    .....  i = j  (모두 커플)

dp[0][0] = abs(man[0] - women[0])
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], abs(man[i] - women[0]))
for j in range(1, m):
    dp[0][j] = min(dp[0][j-1], abs(man[0] - women[j]))

for i in range(1, n):
    for j in range(1, m):
        if i > j:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(man[i] - women[j]))
        elif j > i:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(man[i] - women[j]))
        else:
            dp[i][j] = dp[i-1][j-1] + abs(man[i] - women[j])

print(dp[n-1][m-1])