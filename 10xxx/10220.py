T = int(input())

for _ in range(T):
    N = int(input())
    if N <= 3 or N == 6:
        print(0)
    elif N == 4:
        print(2)
    else:
        print(1)