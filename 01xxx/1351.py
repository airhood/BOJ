N, P, Q = map(int, input().split())

map = dict()

def A(n):
    if n == 0:
        return 1
    if n in map:
        return map[n]
    val =  A(n//P) + A(n//Q)
    map[n] = val
    return val

print(A(N))