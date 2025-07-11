import bisect

N = int(input())
arr = list(map(int, input().split()))

tops = []

for x in arr:
    pos = bisect.bisect_left(tops, x)
    
    if pos == len(tops):
        tops.append(x)
    else:
        tops[pos] = x

print(len(tops))