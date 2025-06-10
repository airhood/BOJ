N = int(input())

if N == 1:
    print(1)
    exit()

fibo = [0] * N
fibo[0] = 1
fibo[1] = 2

for i in range(2, N):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 15746

print(fibo[N-1])