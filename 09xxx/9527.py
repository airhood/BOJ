A, B = map(int, input().split())

dp = [0 for _ in range(59)]

for i in range(1, 59):
    dp[i] = (1 << (i-1)) + (dp[i-1] << 1)

def binary_length(n):
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n >>= 1
        length += 1
    return length

def count(n):
    cnt = 0
    l = binary_length(n)
    for i in range(l):
        k = l-i-1
        if n & (1 << k):
            cnt += dp[k] + (n - (1 << k) + 1)
            n &= ~(1 << k)
    return cnt

print(count(B) - count(A-1))