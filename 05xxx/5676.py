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
        self.tree[i] = self.segment(left, mid, i*2) * self.segment(mid+1, right, i*2+1)
        return self.tree[i]

    def query(self, start, end, left, right, i=1):
        if end < left or start > right:
            return 1
        
        if left <= start and end <= right:
            return self.tree[i]
        
        mid = (start + end) // 2
        return self.query(start, mid, left, right, i*2) * self.query(mid+1, end, left, right, i*2+1)
    
    def update(self, start, end, idx, val, i=1):
        if start > idx or idx > end:
            return self.tree[i]
        
        if start == end:
            self.tree[i] = val
            return self.tree[i]
        
        mid = (start + end) // 2
        self.tree[i] = self.update(start, mid, idx, val, i*2) * self.update(mid+1, end, idx, val, i*2+1)
        return self.tree[i]


while True:
    try:
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        for i in range(N):
            if arr[i] > 0:
                arr[i] = 1
            elif arr[i] < 0:
                arr[i] = -1
            else:
                arr[i] = 0
        seg_tree = MulSegmentTree(arr, N)
        seg_tree.segment(0, N-1)

        ans = ""

        for _ in range(K):
            m, i, j = input().split()
            i = int(i)
            j = int(j)
            if m == "C":
                if j > 0:
                    j = 1
                elif j < 0:
                    j = -1
                else:
                    j = 0
                seg_tree.update(0, N-1, i-1, j)
            elif m == "P":
                result = seg_tree.query(0, N-1, i-1, j-1)
                if result > 0:
                    ans += '+'
                elif result < 0:
                    ans += '-'
                else:
                    ans += '0'
        print(ans)

    except:
        break