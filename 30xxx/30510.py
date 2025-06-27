import math

N = 10**5

def mobius_sieve(n):
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i, n + 1, i):
                prime[j] = False
                mu[j] = -mu[j]
            sq = i * i
            for j in range(sq, n + 1, sq):
                mu[j] = 0
    return mu

mu = mobius_sieve(N)

def get_divisors(n):
    divisors = []
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def phi(n):
    if n == 1:
        return 1
    res = 0
    for d in get_divisors(n):
        res += mu[d] * (n // d)
    return res

P, Q = map(int, input().split())

s = 1
N = Q//P

for i in range(1, N+1):
    s += phi(i)

print(s)