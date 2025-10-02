import sys
sys.setrecursionlimit(10**5)

a, b = map(int, input().split('/'))

def f(a, b):
    if a == 1 and b == 1:
        return
    if a < b:
        print('L', end='')
        f(b-a, a)
    else:
        print('R', end='')
        f(b, a-b)

f(a, b)