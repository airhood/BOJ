n = int(input())

stack = []

i = 1

result = ""

for _ in range(n):
    val = int(input())
    while len(stack) == 0 or stack[-1] != val:
        if len(stack) == 0:
            stack.append(i)
            result += "+"
            i += 1
        elif stack[-1] < val:
            stack.append(i)
            result += "+"
            i += 1
        else:
            print("NO")
            exit()
    stack.pop()
    result += "-"

print("\n".join(result))