import bisect

MOD = 10**9 + 7

class LisSegmentTree:
    def __init__(self, N):
        self.tree = [(0, 0) for _ in range(4*N)]

    def add_size(self, a, b):
        if a[0] > b[0]:
            return a
        elif b[0] > a[0]:
            return b
        else:
            return (a[0], (a[1] + b[1]) % MOD)

    def query(self, start, end, left, right, i=1):
        if end < left or start > right:
            return (0, 0)
        
        if left <= start and end <= right:
            return self.tree[i]
        
        mid = (start + end) // 2
        return self.add_size(self.query(start, mid, left, right, i*2), self.query(mid+1, end, left, right, i*2+1))
    
    def update(self, start, end, idx, val, i=1):
        if start > idx or idx > end:
            return self.tree[i]
        
        if start == end:
            self.tree[i] = self.add_size(self.tree[i], val)
            return self.tree[i]
        
        mid = (start + end) // 2
        self.tree[i] = self.add_size(self.update(start, mid, idx, val, i*2), self.update(mid+1, end, idx, val, i*2+1))
        return self.tree[i]
    
    def getTree(self):
        return self.tree

import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write # 줄바꿈 없음

N = int(input())
arr = list(map(int, input().split()))

unique = sorted(set(arr))
compressed = [bisect.bisect_left(unique, arr[i])+1 for i in range(N)]

segment_tree = LisSegmentTree(len(unique))
for i in range(N):
    val = compressed[i]
    length, count = segment_tree.query(1, len(unique), 1, val-1)
    if length == 0:
        count = 1
    segment_tree.update(1, len(unique), val, (length+1, count))

result = segment_tree.getTree()[1]
print(f"{result[0]} {result[1]}")