N, r, c = map(int, input().split())

ans = 0
for i in range(N-1, -1, -1):
    x = 1 << i
    s = 1 << (2*i)
    q_y = r // x
    q_x = c // x
    r %= x
    c %= x
    if q_x == 0 and q_y == 0:
        pass
    elif q_x == 1 and q_y == 0:
        ans += s
        pass
    elif q_x == 0 and q_y == 1:
        ans += s * 2
        pass
    elif q_x == 1 and q_y == 1:
        ans += s * 3
        pass

print(ans)