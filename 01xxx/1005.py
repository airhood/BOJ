from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    arr = [[] for _ in range(N + 1)]
    inDegree = [0] * (N + 1)
    sum = time[:]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X].append(Y)
        inDegree[Y] += 1
        
    q = deque()
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
    while q:
        x = q.popleft()
        for y in arr[x]:
            inDegree[y] -= 1
            sum[y] = max(sum[y], sum[x] + time[y])
            if inDegree[y] == 0:
                q.append(y)
    W = int(input())
    print(sum[W])
