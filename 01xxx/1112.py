x, b = map(int, input().split())

if x == 0:
    print(0)
    exit()

ans = ''
k = 1
if x < 0 and b > 0:
    x = -x
    k = -1

while x != 0:
    Q, R = x // b, x % b
    if R < 0:
        Q += 1
        R -= b
    ans = str(R) + ans
    x = Q

ans = int(ans) * k
print(ans)