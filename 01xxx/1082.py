N = int(input())
P = list(map(int, input().split()))
M = int(input())

C = []
for i in range(N):
    C.append((P[i], i))

C.sort()

a = []

if N == 1:
    print(0)
    exit()

if N > 1 and C[0][1] == 0:
    if C[1][0] <= M:
        a.append(C[1][1])
        M -= C[1][0]
        pass
    else:
        print('0')
        exit()

for i in range(N):
    if C[i][0] <= M:
        k = M // C[i][0]
        M %= C[i][0]
        for j in range(k):
            a.append(C[i][1])

a.sort(reverse=True)

for i in range(len(a)):
    for j in range(N-1, a[i], -1):
        # a[i]를 j로 바꾸어도 돈이 부족하지 않는다면 교체
        # -> 항상 교체하는 것이 이득이기 때문
        if M + P[a[i]] - P[j] >= 0:
            M += P[a[i]] - P[j]
            a[i] = j
            break

ans = ''
for element in a:
    ans += str(element)

print(ans)