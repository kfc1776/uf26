def add_matrices(A, B):
    C = [[0] * len(A[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract_matrices(A, B):
    C = [[0] * len(A[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C


def matrix_output(matrix):
    m = len(matrix)
    for i in range(m):
        print(*matrix[i])


A = [[1, 10],
     [100, 1000]]
B = [[50, 60],
     [70, 80]]

if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise Exception("Размеры матриц не совпадают")

a_res = add_matrices(A, B)
s_res = subtract_matrices(A, B)

matrix_output(a_res)
matrix_output(s_res)
