N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    arr.sort()
    sum = 0
    for element in arr:
        sum += element
    sum -= arr[-1]
    print(sum)
    exit()

face = 4 * (N-2)*(N-1) + (N-2)*(N-2)
edge = 4 * (N-1) + 4 * (N-2)
vertex = 4

dice = [
    [[], [2, 3], [1, 4], [1, 4], [2, 3], []],
    [[2, 3], [], [0, 5], [0, 5], [], [2, 3]],
    [[1, 4], [0, 5], [], [], [0, 5], [1, 4]],
    [[1, 4], [0, 5], [], [], [0, 5], [1, 4]],
    [[2, 3], [], [0, 5], [0, 5], [], [2, 3]],
    [[], [2, 3], [1, 4], [1, 4], [2, 3], []]
]

face_num = min(arr)

edge_num = 100
for x in range(6):
    for y in range(6):
        k = dice[x][y]
        if len(k) == 0:
            continue

        edge_num = min(edge_num, arr[x] + arr[y])

vertex_num = 150
for x in range(6):
    for y in range(6):
        k = dice[x][y]
        if len(k) == 0:
            continue

        vertex_num = min(vertex_num, min(arr[x] + arr[y] + arr[k[0]], arr[x] + arr[y] + arr[k[1]]))

ans = face * face_num + edge * edge_num + vertex * vertex_num
print(ans)