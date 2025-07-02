import math
import random
from collections import Counter

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
    if miller_rabin(n):
        return n
    
    while True:
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
        
        if d != n:
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

def is_square_num(factors):
    counter = Counter(factors)
    return all(v % 2 == 0 for v in counter.values())

def check_4k3_prime(factors):
    counter = Counter(factors)
    filtered_factors = []
    r = 1

    for p, cnt in counter.items():
        if p % 4 == 3:
            if cnt % 2 == 0:
                r *= math.pow(p, cnt // 2)
            else:
                return (None, None)
        else:
            filtered_factors += [p] * cnt
    return (filtered_factors, r)

def legendre_three_square_available(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 != 7


n = int(input())

if n == 2:
    print(2)
    exit()

factors = prime_factors(n)
if is_square_num(factors):
    # 1개
    print(1)
else:
    filtered_factors, remainder = check_4k3_prime(factors)
    if filtered_factors != None:
        # 2개
        print(2)
    elif legendre_three_square_available(n):
        # 3개
        print(3)
        pass
    else:
        # 4개
        print(4)
        pass