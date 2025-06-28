import random
import math

def miller_rabin(n):
    if n < 2:
        return False
    
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
        
    d = n - 1
    r = 0
    
    while d % 2 == 0:
        d //= 2
        r += 1

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        found = False
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == (n-1):
                found = True
                break
        if not found:
            return False
    
    return True

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    def f(x, c, n):
        return (x*x + c) % n
    
    while d == 1:
        x = f(x, c, n)
        y = f(f(y, c, n), c, n)
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
        
    if miller_rabin(d):
        return d
    else:
        return pollard_rho(d)

def prime_factors(n):
    if n == 1:
        return []
    if miller_rabin(n):
        return [n]
    d = pollard_rho(n)
    return prime_factors(d) + prime_factors(n // d)

def num_divisors(n):
    if n == 1:
        return 1
    
    factors = prime_factors(n)
    factors.sort()
    divisors = 1
    prev = factors[0]
    current = 1
    for i in range(1, len(factors)):
        if factors[i] == prev:
            current += 1
        else:
            divisors *= current + 1
            current = 1
            prev = factors[i]
    divisors *= current + 1
    return divisors

N = int(input())
print(num_divisors(N))