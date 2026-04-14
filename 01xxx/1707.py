import sys
sys.setrecursionlimit(40000)

K = int(input())

LOCAL_RETURN = 0x1234567890
GLOBAL_RETURN = 0x0987654321

for _ in range(K):
    V, E = map(int, input().split())
    g_list = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        g_list[u].append(v)
        g_list[v].append(u)

    parity_list = [2 for _ in range(V+1)]

    def go(a, parity):
        global visited
        global parity_list
        if visited[a] == 1: return
        visited[a] = 1
        for next in g_list[a]:
            if parity_list[next] == parity:
                return GLOBAL_RETURN
        parity_list[a] = parity
        next_parity = 1 if parity == 0 else 0
        for next in g_list[a]:
            result = go(next, next_parity)
            if result == GLOBAL_RETURN:
                return GLOBAL_RETURN
        return LOCAL_RETURN
    
    ans = True
    for v in range(1, V+1):
        result = go(v, 0)
        if result == GLOBAL_RETURN:
            ans = False
            break;

    if ans:
        print("YES")
    else:
        print("NO")