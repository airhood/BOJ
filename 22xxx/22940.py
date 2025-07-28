N = int(input())
mat = [list(map(float, input().split())) for _ in range(N)]

# 행 사다리꼴 행렬 계산
for i in range(N):
    m = mat[i][i]
    for j in range(i, N+1):
        mat[i][j] /= m
    
    for j in range(i+1, N):
        m = mat[j][i]
        for k in range(N+1):
            mat[j][k] -= mat[i][k] * m

# 기약 행 사다리꼴 행렬 계산
for i in range(N-1, 0, -1):
    for j in range(i):
        m = mat[j][i]
        for k in range(N+1):
            mat[j][k] -= mat[i][k] * m

for i in range(N):
    print(round(mat[i][N]), end=' ')