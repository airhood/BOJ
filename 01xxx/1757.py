# N, M = map(int, input().split())
# D = [int(input()) for _ in range(N)]
# D = [0] + D

# dp = [[[0 for _ in range(M+1)] for _ in range(M+1)] for _ in range(N+1)]
# dp[1][1][0] = D[1]

# for i in range(2, N+1):
#     # 연속해서 쉬기
#     a = max(dp[i-1][0])
#     a_idx = dp[i-1][0].index(a)
#     dp[i][0][a_idx+1] = a

#     # 뛰다가 쉬기
#     b = dp[i-1][1][0]
#     dp[i][0][0] = b

#     for j in range(1, M):
#         # 뛰기
#         a = dp[i-1][j-1][0]
#         dp[i][j][0] = a + D[i]

#         # 연속해서 쉬기
#         b = max(dp[i-1][j+1])
#         b_idx = dp[i-1][j+1].index(b)
#         dp[i][j][b_idx+1] = b
    
#     # 뛰기
#     dp[i][M][0] = dp[i-1][j-1][0] + D[M]

# ans = max(dp[N][0])
# print(ans)


# ========================================================


N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
D = [0] + D
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    # 뛰기
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j-1] + D[i]
    
    # j번 쉬기
    for j in range(1, min(i+1, M+1)):
        dp[i][0] = max(dp[i][0], dp[i-j][j], dp[i-j][0])

ans = dp[N][0]
print(ans)