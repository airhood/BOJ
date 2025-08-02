str = ' ' + input()
L = len(str)-1
N = int(input())
words = [input() for _ in range(N)]

INF = 1000000000

dp = [INF for _ in range(L+1)]
dp[0] = 0

def cost(str1, str2):
    if len(str1) != len(str2):
        return 0
    c = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]: c += 1
    return c

for i in range(1, L+1):
    for word in words:
        if len(word) > i + 1: continue
        sub_str = str[i-len(word)+1:i+1]
        if sorted(sub_str) == sorted(word):
            dp[i] = min(dp[i], dp[i-len(word)] + cost(sub_str, word))

if dp[L] == INF:
    print(-1)
else:
    print(dp[L])