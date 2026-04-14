from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

g_list = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    g_list[x].append(y)
    g_list[y].append(x)

queue = []
queue.append((a, 0))

while len(queue) != 0:
    pos = queue[0][0]
    dist = queue[0][1]
    queue.pop(0)

    if (pos == b):
        print(dist, end='')
        exit()
    
    for next in g_list[pos]:
        if not visited[next]:
            visited[next] = True
            queue.append((next, dist + 1))

print(-1)