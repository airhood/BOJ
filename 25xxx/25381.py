inp = list(input())
inp.reverse()

ans = 0

ap = 0
b = 0
c = 0
cc = 0
for i in inp:
    if i == 'B':
        if c > 0:
            c -= 1
            ans += 1
            cc += 1
        else:
            if ap > 0 and cc > 0:
                ap -= 1
                cc -= 1
                ans += 1
            else:
                b += 1
    elif i == 'A':
        if b > 0:
            b -= 1
            ans += 1
        else:
            ap += 1
    elif i == 'C':
        c += 1

print(ans)