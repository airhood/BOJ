import math

class MulSegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (2**(math.ceil(math.log2(N)+1)))

    def segment(self, left, right, i=1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]
        
        mid = (left + right) // 2
        self.tree[i] = (self.segment(left, mid, i*2) * self.segment(mid+1, right, i*2+1)) % DIV
        return self.tree[i]

    def query(self, start, end, left, right, i=1):
        if end < left or start > right:
            return 1
        
        if left <= start and end <= right:
            return self.tree[i]
        
        mid = (start + end) // 2
        return (self.query(start, mid, left, right, i*2) * self.query(mid+1, end, left, right, i*2+1)) % DIV
    
    def update(self, start, end, idx, val, i=1):
        if start > idx or idx > end:
            return self.tree[i]
        
        if start == end:
            self.tree[i] = val
            return self.tree[i]
        
        mid = (start + end) // 2
        self.tree[i] = (self.update(start, mid, idx, val, i*2) * self.update(mid+1, end, idx, val, i*2+1)) % DIV
        return self.tree[i]

DIV = 1000000007

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

tree = MulSegmentTree(arr, N)
tree.segment(0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(0, N-1, b-1, c)
        arr[b-1] = c
    elif a == 2:
        print(tree.query(0, N-1, b-1, c-1))