N = int(input())

fibo = [1, 1]

for i in range(2, N + 2):
    fibo.append(fibo[i-1] + fibo[i-2])

print(2 * fibo[N + 1])