import sys
sys.setrecursionlimit(10**6)

# fast io
import sys, os, io, atexit
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

MOVEMENTS = [[0, -1], [-1, 0], [0, 1], [1, 0]]
check = None

def go(x, y, n, p):
    global check
    if check[x][y]: return None
    n_cnt = n
    p_cnt = p
    for dx, dy in MOVEMENTS:
        next_x = x + dx
        next_y = y + dy
        

def day():
    global check
    check = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            result = go(i, j, 0, 0)
            if result == None: continue
            n, p = result

# solving