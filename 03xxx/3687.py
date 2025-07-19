T = int(input())

stick_min_num = [0, 0, 1, 7, 4, 2, 0, 8]
# stick_min_num[i] -> i개의 성냥으로 만들 수 있는 한 자리 수의 최솟값

INF = int('8' * ((100 // 7) + 1))
dp = [INF] * 101
# dp[i] -> i개의 성냥으로 만들 수 있는 앞자리가 0이 아닌 수의 최솟값
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8

for i in range(8, 101):
    for j in range(2, 8):
        dp[i] = min(dp[i], dp[i-j]*10 + stick_min_num[j])

for _ in range(T):
    n = int(input())

    min_num = dp[n]

    if n % 2 == 0:
        max_num = int('1'*(n//2))
    else:
        max_num = int('7' + '1' * ((n-3)//2))

    print(f"{min_num} {max_num}")