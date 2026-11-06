def read_int():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Введите целое число")


def matrix_input(m, n, ab):
    matrix = [[0] * n for _ in range(m)]

    print("Введите строки матрицы, записывая каждое число через пробел и разделяя строки символом переноса строки")
    for i in range(m):
        try:
            row = list(map(int, input().split()))
        except ValueError:
            print("В строке должны быть только целые числа")
            exit(1)

        if len(row) != n:
            raise ValueError(f"В строке должно быть {n} элементов")

        matrix[i] = row

    return matrix


def matrix_output(matrix, m, n):
    cellwidth = max(len(str(j)) for i in matrix for j in i)

    for i in range(m):
        for j in range(n):
            print(str(matrix[i][j]).ljust(cellwidth, " "), end=" ")
        print()


def matrix_select():
    print("Какая матрица -- A или B? Введите либо A, либо B (с учётом регистра)")
    aorb = input()
    while aorb != "A" and aorb != "B":
        print("Некорректный ввод")
        aorb = input()
    return aorb


def matrix_validity(matrix):
    if matrix == [] or not any(matrix):
        return 0

    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return 0

    return 1


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


def multiply_by_scalar(matrix, scalar):
    B = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = matrix[i][j] * scalar
    return B


def transpose(matrix):
    return [
        [matrix[i][j] for i in range(len(matrix))]
        for j in range(len(matrix[0]))
        ]


def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        return None

    C = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            c = 0
            for k in range(len(A[0])):
                c += A[i][k] * B[k][j]
                C[i][j] = c
    return C


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None

    A = [[int(x) for x in r] for r in matrix]

    det = 1

    for i in range(len(matrix)):
        pivot_r = i
        for k in range(i + 1, len(matrix)):
            if abs(A[k][i]) > abs(A[pivot_r][i]):
                pivot_r = k

        if abs(A[pivot_r][i]) < 1e-9:
            return 0

        if pivot_r != i:
            A[i], A[pivot_r] = A[pivot_r], A[i]
            det *= -1

        det *= A[i][i]

        for k in range(i + 1, len(matrix)):
            factor = A[k][i] / A[i][i]
            for j in range(i, len(matrix)):
                A[k][j] -= factor * A[i][j]

    return round(det, 9)


def inverse_matrix(A, eps=1e-12):
    if len(A) != len(A[0]):
        return None

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
            return None

        AE[i] = [x / pivot for x in AE[i]]

        for r in range(len(A)):
            if r != i:
                factor = AE[r][i]
                AE[r] = [AE[r][j] - factor * AE[i][j]
                    for j in range(2 * len(A))]

    inv_A = [R[len(A):] for R in AE]

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


A = []
B = []

mA = 0
nA = 0

mB = 0
nB = 0

while True:
    print("""
МАТРИЧНЫЙ КАЛЬКУЛЯТОР

1. Ввести матрицу
2. Вывести матрицу
3. Сложить две матрицы (A + B)
4. Вычесть две матрицы (A - B)
5. Умножить матрицу на число
6. Транспонировать матрицу
7. Умножить две матрицы (A * B)
8. Найти определитель
9. Найти обратную матрицу
10. Вывести характеристики матрицы
0. Завершить программу
             """)
    sel = read_int()

    match sel:
        case 0:
            break
        case 1:
            aorb = matrix_select()
            print(f"Введите числа m{aorb} и n{aorb} через строку")
            if aorb == "A":
                mA = read_int()
                nA = read_int()

                if mA <= 0 or nA <= 0:
                    print("Числа, равные количествам строк и столбцов, должны быть > 0")
                    mA, nA = 0, 0
                    continue

                A = matrix_input(mA, nA, 1)
                print("Введена матрица A")
            elif aorb == "B":
                mB = read_int()
                nB = read_int()

                if mB <= 0 or nB <= 0:
                    print("Числа, равные количествам строк и столбцов, должны быть > 0")
                    mB, nB = 0, 0
                    continue

                B = matrix_input(mB, nB, 2)
                print("Введена матрица B")
        case 2:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                if aorb == "A":
                    matrix_output(A, mA, nA)
                elif aorb == "B":
                    matrix_output(B, mB, nB)
            else:
                print(f"Матрица {aorb} пустая или не является прямоугольной")
        case 3:
            if matrix_validity(A) and matrix_validity(B):
                if len(A) == len(B) and len(A[0]) == len(B[0]):
                    C = add_matrices(A, B)
                    print("A + B =")
                    matrix_output(C, len(C), len(C[0]))
                else:
                    print("Размеры матриц A и B не совпадают")
            else:
                print("Матрица A или B пустая или не прямоугольная")
        case 4:
            if matrix_validity(A) and matrix_validity(B):
                if len(A) == len(B) and len(A[0]) == len(B[0]):
                    C = subtract_matrices(A, B)
                    print("A - B =")
                    matrix_output(C, len(C), len(C[0]))
                else:
                    print("Размеры матриц A и B не совпадают")
            else:
                print("Матрица A или B пустая или не прямоугольная")
        case 5:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                print("Введите скаляр")
                k = read_int()

                print(f"k * {aorb} =")
                C = multiply_by_scalar(A if aorb == "A" else B, k)

                matrix_output(C, len(C), len(C[0]))
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
        case 6:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                C = transpose(A if aorb == "A" else B)
                matrix_output(C, len(C), len(C[0])) 
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
        case 7:
            if matrix_validity(A) and matrix_validity(B):
                C = multiply_matrices(A, B)
                if C is not None:
                    matrix_output(C, len(C), len(C[0]))
                else:
                    print("Матрицу A нельзя умножить на B")
            else:
                print("Матрица A или B пустая или не прямоугольная")
        case 8:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                C = determinant(A if aorb == "A" else B)
                if C is None:
                    print("Матрица не квадратная")
                    continue
                print(C)
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
        case 9:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                C_raw = inverse_matrix(A if aorb == "A" else B)
                if C_raw is None:
                    print(f"Матрица {aorb} не квадратная или для неё не существует обратной матрицы")
                    continue
                C = [[round(y, 12) for y in x] for x in C_raw]

                if not is_identity(
                        multiply_matrices(
                            A if aorb == "A" else B,
                            C)):
                    print("Не удалось найти обратную матрицу")
                    continue

                matrix_output(C, len(C), len(C[0]))
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
        case 10:
            aorb = matrix_select()

            X = A if aorb == "A" else B

            if matrix_validity(X):
                min_X = X[0][0]
                max_X = X[0][0]
                sum_X = 0

                row_sums_X = []
                col_sums_X = []

                for i in range(len(X)):
                    for j in range(len(X[0])):
                        min_X = X[i][j] if X[i][j] < min_X else min_X
                        max_X = X[i][j] if X[i][j] > max_X else max_X
                        sum_X += X[i][j]
                    row_sums_X.append(sum(X[i]))

                X_T = transpose(X)

                for i in range(len(X_T)):
                    col_sums_X.append(sum(X_T[i]))

                print(f"Размер: {len(X)} x {len(X[0])}")
                print("Минимальный элемент:", min_X)
                print("Максимальный элемент:", max_X)
                print("Сумма элементов:", sum_X)
                print("Среднее значение:", sum_X / (len(X) * len(X[0])))
                print()
                print("Суммы строк:", ', '.join(map(str, row_sums_X)))
                print("Суммы столбцов:", ', '.join(map(str, col_sums_X)))
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
