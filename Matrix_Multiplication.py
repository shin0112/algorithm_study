def Matrix_Multiplication(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]  # c = [[0] * n] * n ?
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


matrix_a = [[1, 1], [1, 1]]
matrix_b = [[1, 1], [1, 1]]
matrix_c = Matrix_Multiplication(matrix_a, matrix_b)  # 7 10 15 22

matrix_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_e = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
matrix_f = Matrix_Multiplication(matrix_d, matrix_e)

for i in matrix_c:
    for j in i:
        print(j, end=" ")
    print()

print()

for i in matrix_f:
    for j in i:
        print(j, end=" ")
    print()
