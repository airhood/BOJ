N = int(input())
P = list(map(int, input().split()))

# xor은 연산 순서 상관 없다.
# xor은 2번 연산하면 원래대로 돌아옴

g = 0
for p in P:
    g ^= p

ans = 0
for i in range(N):
    for j in range(P[i]):
        a = j
        a ^= g
        a ^= P[i]
        if a == 0:
            ans += 1

print(ans)