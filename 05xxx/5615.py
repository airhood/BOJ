import random

def miller_rabin(n, k=5):
    if n < 2:
        return False
    
    for p in [2, 3, 5, 7, 11, 13]:
        if n % p == 0:
            return n == p
        
    d = n - 1
    r = 0
    
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x in (1, n-1):
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


N = int(input())
count = 0
for _ in range(N):
    S = int(input())
    num = 2*S + 1
    if miller_rabin(num):
        count += 1

print(count)