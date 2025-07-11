DIV = 1000000007

n = int(input())

fibo = [[0, 1],
     [1, 1]]

def multiply(mat1, mat2):
    return [
        [(mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % DIV,
         (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % DIV],
        [(mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % DIV,
         (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % DIV]
    ]

def pow(mat, n):
    if n > 1:
        mat1 = pow(mat, n//2)
        mat1 = multiply(mat1, mat1)
        mat1[0][0] %= DIV
        mat1[0][1] %= DIV
        mat1[1][0] %= DIV
        mat1[1][1] %= DIV

        if n % 2 == 1:
            mat1 = multiply(mat1, mat)
            mat1[0][0] %= DIV
            mat1[0][1] %= DIV
            mat1[1][0] %= DIV
            mat1[1][1] %= DIV
    else:
        mat1 = mat
    return mat1

print(pow(fibo, n)[0][1] % DIV)