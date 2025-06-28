N = int(input())

print(2**N - 1)
for K in range(1, 2**N):
    A = ((K & (K - 1)) % 3) + 1
    B = (((K | (K - 1)) + 1) % 3) + 1

    if N % 2 == 0:
        if A == 2: A = 3
        elif A == 3: A = 2
        if B == 2: B = 3
        elif B == 3: B = 2
    
    print(f"{A} {B}")