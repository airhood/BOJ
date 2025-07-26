N, M = map(int, input().split())

"""
start: (1, 2), (2, 1)
finish: (N, M-1), (N-1, M)

{(N+M-4)C(M-2)}^2 - {{(N+M-4)C(N-1)} * {(N+M-4)C(M-1)}}
"""

MOD = 1_000_000_007

K = N+M

fact = [1] * (K + 1)
fact_inv = [1] * (K + 1)

for i in range(1, K+1):
    fact[i] = (fact[i-1] * i) % MOD

fact_inv[K] = pow(fact[K], MOD-2, MOD)
for i in range(K, 0, -1):
    fact_inv[i-1] = (fact_inv[i] * i) % MOD

def nCr(n, r, fact, inv_fact):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

ans = ((pow(nCr(N+M-4, M-2, fact, fact_inv), 2, MOD) - (nCr(N+M-4, N-1, fact, fact_inv) * nCr(N+M-4, M-1, fact, fact_inv))) * 2) % MOD
print(ans)