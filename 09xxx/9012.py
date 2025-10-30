N = int(input())

for _ in range(N):
    inp = input()
    d = 0
    for i in inp:
        if i == '(':
            d += 1
        elif i == ')':
            d -= 1

        if d < 0:
            break
    
    if d == 0:
        print("YES")
    else:
        print("NO")
