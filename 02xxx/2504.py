inp = input()

stack = []

ans = [0]

last = ''

for i in inp:
    if i == '(':
        stack.append('(')
        ans.append(0)
        last = '('
    elif i == ')':
        if len(stack) == 0:
            print(0)
            exit()
        if stack[-1] == '(':
            stack.pop()
            a = ans.pop()
            ans[-1] += a * 2
            if last == '(': ans[-1] += 2
        else:
            print(0)
            exit()
        last = ')'
    elif i == '[':
        stack.append('[')
        ans.append(0)
        last = '['
    elif i == ']':
        if len(stack) == 0:
            print(0)
            exit()
        if stack[-1] == '[':
            stack.pop()
            a = ans.pop()
            ans[-1] += a * 3
            if last == '[': ans[-1] += 3
        else:
            print(0)
            exit()
        last = ']'

if len(stack) != 0:
    print(0)
    exit()

print(ans[0])