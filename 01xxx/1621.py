N = int(input())
K, C = map(int, input().split())
inp = list(map(int, input().split()))

if N == 1:
    if C < inp[0]:
        print(C)
        print(1)
        print(1)
    else:
        print(inp[0])
        print(0)
    exit()

if K == 1:
    t = 0
    kp = []
    for i in range(N):
        if C < inp[i]:
            kp.append(i + 1)
            t += C
        else:
            t += inp[i]
    print(t)
    print(len(kp))
    for i in range(len(kp)):
        print(kp[i], end=" ")
    exit()

kp = [-1]

for i in range(1, K - 1):
    inp[i] += inp[i - 1]
    kp.append(-1)

for i in range(K - 1, N):
    A = inp[i - 1] + inp[i]

    if i == K - 1:
        B = C
    else:
        B = inp[i - K] + C

    if A <= B:
        inp[i] = A
        kp.append(kp[i - 1])
    else:
        inp[i] = B
        kp.append(i - K + 1)

print(inp[-1])

k_pos = []
ki = len(kp) - 1
while kp[ki] != -1 and ki >= 0:
    k_pos.append(kp[ki] + 1)
    ki = kp[ki] - 1

print(len(k_pos))
for i in range(len(k_pos) - 1, -1, -1):
    print(k_pos[i], end=" ")