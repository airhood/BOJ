import math

class MinSegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (2**(math.ceil(math.log2(N)+1)))

    def segment(self, left, right, i=1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]
        
        mid = (left + right) // 2
        self.tree[i] = min(self.segment(left, mid, i*2), self.segment(mid+1, right, i*2+1))
        return self.tree[i]

    def query(self, start, end, left, right, i=1):
        if end < left or start > right:
            return INF
        
        if left <= start and end <= right:
            return self.tree[i]
        
        mid = (start + end) // 2
        return min(self.query(start, mid, left, right, i*2), self.query(mid+1, end, left, right, i*2+1))
    
    def update(self, start, end, idx, val, i=1):
        if start > idx or idx > end:
            return self.tree[i]
        
        if start == end:
            self.tree[i] = val
            return self.tree[i]
        
        mid = (start + end) // 2
        self.tree[i] = min(self.update(start, mid, idx, val, i*2), self.update(mid+1, end, idx, val, i*2+1))
        return self.tree[i]
    
    def t(self):
        return self.tree
    
class MaxSegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (2**(math.ceil(math.log2(N)+1)))

    def segment(self, left, right, i=1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]
        
        mid = (left + right) // 2
        self.tree[i] = max(self.segment(left, mid, i*2), self.segment(mid+1, right, i*2+1))
        return self.tree[i]

    def query(self, start, end, left, right, i=1):
        if end < left or start > right:
            return 0
        
        if left <= start and end <= right:
            return self.tree[i]
        
        mid = (start + end) // 2
        return max(self.query(start, mid, left, right, i*2), self.query(mid+1, end, left, right, i*2+1))
    
    def update(self, start, end, idx, val, i=1):
        if start > idx or idx > end:
            return self.tree[i]
        
        if start == end:
            self.tree[i] = val
            return self.tree[i]
        
        mid = (start + end) // 2
        self.tree[i] = max(self.update(start, mid, idx, val, i*2), self.update(mid+1, end, idx, val, i*2+1))
        return self.tree[i]

INF = 1000000001

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

min_tree = MinSegmentTree(arr, N)
min_tree.segment(0, N-1)

max_tree = MaxSegmentTree(arr, N)
max_tree.segment(0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    min_val = min_tree.query(0, N-1, a-1, b-1)
    max_val = max_tree.query(0, N-1, a-1, b-1)
    print(f"{min_val} {max_val}")