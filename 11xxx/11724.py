import sys
V, E = map(int, input().split())

sys.setrecursionlimit(2000)

g_list = [[] for _ in range(V+1)]
check = [0 for _ in range(V+1)]

for _ in range(E):
    u, v = map(int, input().split())
    g_list[u].append(v)
    g_list[v].append(u)

def go(a):
    if check[a] == 1: return
    check[a] = 1
    for next in g_list[a]:
        go(next)

cc = 0

for v in range(1, V+1):
    if check[v] == 1: continue
    go(v)
    cc += 1

print(cc)