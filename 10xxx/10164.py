N, M, K = map(int, input().split())

def calc(a, b):
    result = 1
    for i in range(a + 1, a + b + 1):
        result *= i
    div = 1
    for i in range(1, b + 1):
        div *= i
    result //= div
    return result

NK = (K - 1) // M + 1
MK = K % M
if MK == 0:
    MK = M

if K == 0:
    print(calc(N-1, M-1))
else:
    print(calc(NK-1, MK-1) * calc(N-NK, M-MK))