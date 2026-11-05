def inverse_matrix(A, eps=1e-12):
    E = identity_matrix(len(A))

    AE = []
    for i in range(len(A)):
        AE.append(A[i] + E[i])
    
    for i in range(len(A)):
            pivot_r = i
            for r in range(i + 1, len(A)):
                if abs(AE[r][i]) > abs(AE[pivot_r][i]):
                    pivot_r = r
                    
            AE[i], AE[pivot_r] = AE[pivot_r], AE[i]
    
            pivot = AE[i][i]
            
            if abs(pivot) < eps:
                raise ValueError("обратной матрицы не существует")
    
            AE[i] = [x / pivot for x in AE[i]]
    
            for r in range(len(A)):
                if r != i:
                    factor = AE[r][i]
                    AE[r] = [AE[r][j] - factor * AE[i][j] for j in range(2 * len(A))]
    
    inv_A = [R[len(A):] for R in AE]

    #return list(map(lambda x: list(map(lambda y: round(y, 9), x)), inv_A))
    return inv_A


def identity_matrix(n):
    E = [[0.0] * n for _ in range(n)]
    for i in range(n):
        E[i][i] = 1.0
    return E


def is_identity(matrix, eps=1e-12):
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[0])):
            expected = 1.0 if i == j else 0.0
            if abs(matrix[i][j] - expected) >= eps:
                return False
    return True


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


A = [[1.0, 2.0, 3.0],
     [4.0, 5.0, 6.0],
     [7.0, 8.0, 10.0]]

if len(A) != len(A[0]):
    raise Exception("матрица не квадратная")

inv_A = inverse_matrix(A)
inv_A_rounded = [[round(y, 9) for y in x] for x in inv_A]

check_matrix = matrix_multiplication(A, inv_A)

if is_identity(check_matrix):
    print("ура! произведение матриц является единичной матрицей (в пределах погрешности).")
else:
    print(":( произведение матриц НЕ является единичной матрицей!")

inv_A_len = []
for i in range(len(inv_A_rounded)):
    for j in range(len(inv_A_rounded[0])):
        inv_A_len.append(len(str(inv_A_rounded[i][j])))

inv_A_len_max = max(inv_A_len)

for i in range(len(inv_A)):
    for j in range(len(inv_A[0])):
        print(str(inv_A_rounded[i][j]).rjust(inv_A_len_max), end = " ")
    print()
