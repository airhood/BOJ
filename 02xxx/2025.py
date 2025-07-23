import math

N = int(input())
sx, sy = map(int, input().split())

board = [[-1 for _ in range(N)] for _ in range(N)]
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


def inBoard(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

def countMoves(x, y):
    count = 0
    for i in range(8):
        next_x = x + moves[i][0]
        next_y = y + moves[i][1]
        if (inBoard(next_x, next_y) and board[next_x][next_y] == -1):
            count += 1
    return count

def distanceCenter(x, y):
    cx, cy = (N-1) / 2, (N-1) / 2
    dx = x - cx
    dy = y - cy
    return math.sqrt(dx * dx + dy * dy)

def warnsdorff(x_start, y_start):
    x, y = x_start, y_start
    steps = []
    for step in range(N*N):
        board[x][y] = step
        steps.append((x, y))

        next = []

        for i in range(8):
            next_x = x + moves[i][0]
            next_y = y + moves[i][1]
            if (inBoard(next_x, next_y) and board[next_x][next_y] == -1):
                deg = countMoves(next_x, next_y)
                dist = distanceCenter(next_x, next_y)
                next.append((deg, dist, (next_x, next_y)))
            
        if len(next) == 0:
            if step != N*N - 1:
                return None
        else:
            next.sort(key=lambda x: (x[0], -x[1]))
            x = next[0][2][0]
            y = next[0][2][1]

    return steps

result = warnsdorff(sx - 1, sy - 1)

if result == None:
    print(-1)
    exit()

for x, y in result:
    print(f"{x+1} {y+1}")