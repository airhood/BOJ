import math
import random

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

A, B = map(int, input().split())
ans = ""
for x in range(A, B+1):
    if x == 1:
        continue
    if x % 2 == 0:
        continue
    if x == 9:
        ans += f"{x} "
    elif miller_rabin(x):
        ans += f"{x} "

print(ans)