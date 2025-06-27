def phi(cur):
    e = cur
    for i in range(2, int(cur**(1/2) + 1)):
        if cur % i == 0:
            e //= i; e *= i - 1
            while cur % i == 0:
                cur //= i
    
    if cur > 1: e //= cur; e *= cur - 1
    return e

N = int(input())

if N == 1 or N == 2: print(N)
elif N % 2 == 1: print(-1)
else:
    arr = [1, 2]
    for i in range(3, int(N**(1/2)) + 1):
        if (N % i == 0):
            arr.append(i)
            if (N // i != i):
                arr.append(N // i)
    
    result = -1
    for i in range(2, len(arr)):
        if phi(arr[i]) * arr[i] == N:
            result = arr[i]
            break

    print(result)