
def make_min_factor(n):
    min_factor = [0] * (n + 1)
    for i in range(2, n + 1):
        if min_factor[i] == 0:
            for j in range(i, n + 1, i):
                if min_factor[j] == 0:
                    min_factor[j] = i
    return min_factor

def prime_factors(n, min_factor):
    factors = []
    while n > 1:
        factors.append(min_factor[n])
        n //= min_factor[n]
    return factors


import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
K = list(map(int, input().split()))

min_factor = make_min_factor(max(K))

for k in K:
    factors = prime_factors(k, min_factor)
    print(' '.join(map(str, factors)))