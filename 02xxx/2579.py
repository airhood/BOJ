N = int(input())

list = []
dp = [0] * N;

for _ in range(N):
    temp = int(input())
    list.append(temp)

if N == 1:
    print(list[0])
    exit()

dp[0] = list[0]
dp[1] = list[0] + list[1]

for i in range(2, N):
    dp[i] = max(dp[i-3] + list[i-1] + list[i], dp[i-2] + list[i]);

print(dp[-1]);