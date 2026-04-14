import sys
sys.setrecursionlimit(10**5)

# fast io
import sys, os, io, atexit
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def condition(r1, c1, r2, c2):
    global A, L, R
    temp = abs(A[r1][c1] - A[r2][c2])
    if temp >= L and temp <= R:
        return True
    return False

def safe(nr, nc):
    global A
    if nr < 1 or nr > N: return False
    if nc < 1 or nc > N: return False
    return True

def dfs(r, c, n):
    global check, total, cnt, G, A, dx, dy
    G[n].append([r, c])
    check[r][c] = 1
    total[n] += A[r][c]
    cnt[n] += 1
    for i in range(4):
        next_r = r + dx[i]
        next_c = c + dy[i]
        if safe(next_r, next_c) and not check[next_r][next_c]:
            if condition(r, c, next_r, next_c):
                dfs(next_r, next_c, n)

N, L, R = map(int, input().split())
A = [[0]*(N+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    A.append([0] + list(map(int, input().split())))
idx = 0
ans = 0
while idx < N*N:
    idx = 0
    check = [[0 for _ in range(N+1)] for _ in range(N+1)]
    total = [0]*((N+1)**2)
    cnt = [0]*((N+1)**2)
    G = [[] for _ in range((N+1)**2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not check[i][j]:
                dfs(i, j, idx)
                idx += 1
    for i in range(idx):
        avg = total[i] // cnt[i]
        for j in G[i]:
            A[j[0]][j[1]] = avg
    ans += 1

print(ans - 1)