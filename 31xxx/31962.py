N, X = map(int, input().split())

mx = -1
for _ in range(N):
    S, T = map(int, input().split())
    if S + T > X: continue
    mx = max(mx, S)

print(mx)