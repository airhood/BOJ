import sys
input = sys.stdin.readline

def phi(cur):
    e = cur
    for i in range(2, int(cur**(1/2) + 1)):
        if cur % i == 0:
            e //= i; e *= i - 1
            while cur % i == 0:
                cur //= i
    
    if cur > 1: e //= cur; e *= cur - 1
    return e

dp = [0]
count = 0

P = int(input())
arr = [int(input()) for _ in range(P)]
for N in arr:
    for i in range(count + 1, N+1):
        dp.append(dp[i-1] + phi(i))
        count = N

    print(dp[N]+1)