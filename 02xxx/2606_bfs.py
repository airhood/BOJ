V = int(input())
E = int(input())

g_list = [[] for _ in range(V+1)]
check = [0 for _ in range(V+1)]
exploit = 0

for _ in range(E):
    u, v = map(int, input().split())
    g_list[u].append(v)
    g_list[v].append(u)

def bfs(k):
    global check
    global V, exploit
    q = []
    check[k] = 1
    q.append(k)
    while len(q) > 0:
        cur = q[0]
        q.pop(0)
        for i in g_list[cur]:
            if not check[i]:
                check[i] = 1
                exploit += 1
                q.append(i)

bfs(1)
print(exploit)