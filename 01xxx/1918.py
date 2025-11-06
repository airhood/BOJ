
depth = 0

def convert(x):
    if x == '+' or x == '-': return 1 + 10 * depth
    elif x == '*' or x == '/': return 2 + 10 * depth
    else: return 0

def check_bracket(x):
    global depth
    if x == '(':
        depth += 1
        return True
    elif x == ')':
        depth -= 1
        return True
    else: return False

inp = input()
s = []

for i in inp:
    if check_bracket(i): continue

    if convert(i):
        while s and s[-1][1] >= convert(i):
            print(s.pop()[0], end='')
        s.append([i, convert(i)])
    else:
        print(i, end='')
while s:
    print(s.pop()[0], end='')