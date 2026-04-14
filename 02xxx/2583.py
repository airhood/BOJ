import sys
sys.setrecursionlimit(10**5)

M, N, K = map(int, input().split())

grid = [[1 for _ in range(M)] for _ in range(N)]

MOVEMENTS = [[0, -1], [-1, 0], [0, 1], [1, 0]]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 0

def find(x, y):
    count = 0
    for movement in MOVEMENTS:
        next_x = x + movement[0]
        next_y = y + movement[1]

        if (next_x >= N or next_x < 0 or next_y >= M or next_y < 0):
            continue

        if grid[next_x][next_y] == 1:
            count += 1
            grid[next_x][next_y] = 2
            sub_count = find(next_x, next_y)
            count += sub_count
    
    return count

house_count = []

for x in range(N):
    for y in range(M):
        if grid[x][y] == 1:
            grid[x][y] = 2
            count = find(x, y) + 1
            house_count.append(count)

house_count.sort()

print(len(house_count))

print(' '.join([str(element) for element in house_count]))