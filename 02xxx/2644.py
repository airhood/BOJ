N = int(input())
a, b = map(int, input().split())
M = int(input())
G = [[] for _ in range(N+1)]
check = [-1 for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

def dfs(idx, r):
    global check
    if check[idx] != -1: return
    check[idx] = r
    for next in G[idx]:
        dfs(next, r+1)

dfs(a, 0)
print(check[b])