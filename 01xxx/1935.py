N = int(input())
inp = input()
s = []

op = ['+', '-', '*', '/']

val = [float(input()) for _ in range(N)]

for i in inp:
    if i in op:
        b, a = s.pop(), s.pop()
        if not isinstance(a, float):
            a = val[ord(a)-ord('A')]
        if not isinstance(b, float):
            b = val[ord(b)-ord('A')]
        s.append(float(eval(f"{a}{i}{b}")))
    else:
        s.append(i)

if not isinstance(s[0], float):
    s.append(val[ord(s.pop())-ord('A')])

print(f"{s[0]:.2f}")