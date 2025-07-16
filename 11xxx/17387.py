x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)

def CCW(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

P = CCW(A, B, C) * CCW(A, B, D)
Q = CCW(C, D, A) * CCW(C, D, B)

if P == 0 and Q == 0:
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C

    if C <= B and A <= D:
        print(1)
    else:
        print(0)
elif P <= 0 and Q <= 0:
    print(1)
else:
    print(0)