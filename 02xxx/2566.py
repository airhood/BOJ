inp = [list(map(int, input().split())) for i in range(9)]

p, q = 0, 0

max_val = 0
for i in range(9):
    for j in range(9):
        max_val = max(max_val, inp[i][j])
        if inp[i][j] == max_val:
            p, q = i, j

print(max_val)
print(f"{p+1} {q+1}")