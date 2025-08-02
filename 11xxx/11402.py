N, K, M = map(int, input().split())

arr = [[0 for _ in range(M+1)] for _ in range(M+1)]

for i in range(M+1):
    for j in range(i+1):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = (arr[i-1][j] + arr[i-1][j-1]) % M

ans = 1
while N != 0 and K != 0:
    ans *= arr[N % M][K % M]
    ans %= M
    N //= M
    K //= M

print(ans)