N, K = map(int, input().split())
W = []
V = []

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

arr = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N+1):
    for w in range(K+1):
        if i == 0 or w == 0:
            arr[i][w] = 0
        elif W[i-1] <= w:
            arr[i][w] = max(V[i-1] + arr[i-1][w-W[i-1]], arr[i-1][w])
        else:
            arr[i][w] = arr[i-1][w]

print(arr[N][K])