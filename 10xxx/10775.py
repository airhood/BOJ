import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

arr = [int(input()) for _ in range(P)]

parent = [i for i in range(G+1)]

def find(x):
    y = x
    while y != parent[y]:
        y = parent[y]
    parent[x] = y
    return y

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x == parent_y: return
    elif parent_x > parent_y:
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x

for i in range(P):
    if find(arr[i]) == 0:
        print(i)
        exit()
    else:
        union(find(arr[i])-1, find(arr[i]))
print(P)