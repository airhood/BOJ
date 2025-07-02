N = int(input())

arr = [0] * N

for i in range(N):
    coins = input().strip()
    for j in range(N):
        if coins[j] == 'T':
            arr[i] += (1 << j)

def col(row):
  for i in range(N):
    if row & (1 << i):
      arr[i] = ~arr[i] & ((1 << N) - 1)

def cal(row):
  value = 0
  col(row)
  for i in range(N):
    cols = 0
    for j in range(N):
      if arr[j] & (1 << i):
        cols += 1
    value += min(cols, N-cols)
  col(row)
  return value

ans = 2**N

for i in range(2**N):
   ans = min(ans, cal(i))

print(ans)