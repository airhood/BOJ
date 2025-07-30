from collections import deque

def topology_sort(N, arr, inDegree):
    result = []
    q = deque()
    for i in range(1, N+1):
        if inDegree[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        result.append(x)
        for j in arr[x]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                q.append(j)
    
    if len(result) != N:
        return None
    return result

N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)
for _ in range(M):
    K = list(map(int, input().split()))
    if K[0] < 2: continue
    for i in range(2, K[0]+1):
        if graph[K[i-1]][K[i]] == 1: continue
        arr[K[i-1]].append(K[i])
        inDegree[K[i]] += 1
        graph[K[i-1]][K[i]] = 1

result = topology_sort(N, arr, inDegree)

if result == None:
    print(0)
else:
    for r in result:
        print(r)