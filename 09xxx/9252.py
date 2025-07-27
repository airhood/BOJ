str1 = input()
str2 = input()

N, M = len(str1), len(str2)

str1 = ' ' + str1
str2 = ' ' + str2

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs = []

i, j = N, M
while dp[i][j] != 0:
    if dp[i-1][j] == dp[i][j]:
        i -= 1
    elif dp[i][j-1] == dp[i][j]:
        j -= 1
    else:
        lcs.append(str1[i]) # str2[j]를 append해도 상관없음 (어짜피 두 값이 같음)
        i -= 1
        j -= 1

lcs.reverse()

print(dp[N][M])
print(''.join(lcs))