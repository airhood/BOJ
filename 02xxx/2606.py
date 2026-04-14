V = int(input())
E = int(input())

adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
check = [0 for _ in range(V+1)]
exploit = 0

for _ in range(E):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1

def worm(a):
    global check
    global exploit
    if check[a] == 1: return
    exploit += 1
    check[a] = 1
    for i in range(len(adj[a])):
        if adj[a][i] == 1:
            worm(i)

worm(1)
exploit -= 1 # 숙주 1번 제외
print(exploit)