from collections import deque

def sliding_window_min(N, L, A):
    dq = deque()
    result = []

    for i in range(N):
        while dq and dq[0] < i - L + 1:
            dq.popleft()

        while dq and A[dq[-1]] > A[i]:
            dq.pop()

        dq.append(i)

        result.append(A[dq[0]])

    return result

N, L = map(int, input().split())
A = list(map(int, input().split()))

D = sliding_window_min(N, L, A)
for d in D:
    print(d, end=' ')