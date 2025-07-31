import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

arr.sort(key=lambda x: x[2])


parent = [i for i in range(N+1)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x == parent_y: return
    elif parent_x > parent_y:
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x

ans = 0
max_c = 0
for a, b, c in arr:
    if find(a) != find(b):
        union(a, b)
        ans += c
        max_c = c
ans -= max_c
print(ans)