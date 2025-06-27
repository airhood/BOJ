def phi(cur):
    e = cur
    for i in range(2, int(cur**(1/2) + 1)):
        if cur % i == 0:
            e //= i; e *= i - 1
            while cur % i == 0:
                cur //= i
    
    if cur > 1: e //= cur; e *= cur - 1
    return e

print(phi(int(input())))