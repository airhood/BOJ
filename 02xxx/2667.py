N = int(input())
map = [list(map(int, input())) for _ in range(N)]

MOVEMENTS = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def find(x, y):
    count = 0
    for movement in MOVEMENTS:
        next_x = x + movement[0]
        next_y = y + movement[1]

        if (next_x >= N or next_x < 0 or next_y >= N or next_y < 0):
            continue

        if map[next_x][next_y] == 1:
            count += 1
            map[next_x][next_y] = 2
            sub_count = find(next_x, next_y)
            count += sub_count
    
    return count

house_count = []

for x in range(N):
    for y in range(N):
        if map[x][y] == 1:
            map[x][y] = 2
            count = find(x, y) + 1
            house_count.append(count)

house_count.sort()

print(len(house_count))

for count in house_count:
    print(count)