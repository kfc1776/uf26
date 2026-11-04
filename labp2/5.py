def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        raise Exception("такие матрицы не умножаются!!!")

    C = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            c = 0
            for k in range(len(A[0])):
                c += A[i][k] * B[k][j]
                C[i][j] = c
    return C


# X   * Y   = Z
# AxB   BxC   AxC

X = [[1, 2, 3],
     [4, 5, 6]]
Y = [[7, 8],
     [9, 10],
     [11, 12]]

for i in matrix_multiplication(X, Y):
    print(*i)
