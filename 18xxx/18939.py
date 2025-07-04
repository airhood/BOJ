T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    if M < 2*K:
        print("Yuto")
        continue
    S = (N*M) - 2 * (K*K)
    if S % 2 == 1:
        print("Yuto")
    else:
        print("Platina")