V = int(input())
E = int(input())

g_list = [[] for _ in range(V+1)]
check = [0 for _ in range(V+1)]
exploit = 0

for _ in range(E):
    u, v = map(int, input().split())
    g_list[u].append(v)
    g_list[v].append(u)

def worm(a):
    global check
    global exploit
    if check[a] == 1: return
    exploit += 1
    check[a] = 1
    for next in g_list[a]:
        worm(next)

worm(1)
exploit -= 1 # 숙주 1번 제외
print(exploit)