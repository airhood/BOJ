arr = [list(map(int, input())) for _ in range(9)]

check_h = [[0 for _ in range(10)] for _ in range(10)]
check_v = [[0 for _ in range(10)] for _ in range(10)]
check_b = [[0 for _ in range(10)] for _ in range(10)]

def block_idx(x, y):
    return (x//3)*3+(y//3)

for i in range(9):
    for j in range(9):
        if arr[i][j] != 0:
            check_h[i][arr[i][j]] = 1
            check_v[j][arr[i][j]] = 1
            check_b[block_idx(i, j)][arr[i][j]] = 1

def sudoku(idx):
    if idx == 81:
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end='')
            print('')
        return True
    
    x = idx // 9
    y = idx % 9

    if arr[x][y] != 0:
        return sudoku(idx+1)
    else:
        for k in range(1, 10):
            if (check_h[x][k] == 0 and check_v[y][k] == 0 and check_b[block_idx(x, y)][k] == 0):
                check_h[x][k] = 1
                check_v[y][k] = 1
                check_b[block_idx(x, y)][k] = 1
                arr[x][y] = k
                
                if (sudoku(idx+1)):
                    return True
                else:
                    arr[x][y] = 0
                    check_h[x][k] = 0
                    check_v[y][k] = 0
                    check_b[block_idx(x, y)][k] = 0
    return False

sudoku(0)