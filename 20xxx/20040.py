n, m = map(int, input().split())

parent = [i for i in range(n)]

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

for i in range(m):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print(i+1)
        exit()
    union(x, y)
print(0)