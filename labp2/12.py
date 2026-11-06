def matrix_input(m, n, ab):
    global maxelementA
    global maxelementB

    matrix = [[0] * n for _ in range(m)]

    print("Введите строки матрицы, записывая каждое число через пробел и разделяя строки символом переноса строки")
    for i in range(m):
        try:
            row = list(map(int, input().split()))
        except ValueError:
            print("В строке должны быть только целые числа")
            exit(1)

        if len(matrix[i]) != n:
            raise ValueError(f"В строке должно быть {n} элементов")

        matrix[i] = row

        for j in range(n):
            if ab == 1:
                if matrix[i][j] > maxelementA:
                    maxelementA = matrix[i][j]
            if ab == 2:
                if matrix[i][j] > maxelementB:
                    maxelementB = matrix[i][j]

    return matrix


def matrix_output(matrix, m, n, cellwidth):
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


def findmax_matrix(matrix):
    m = matrix[0][0]
    for i in matrix:
        for j in i:
            if j > maxelementC:
                m = j
    return m


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
        print("Матрицу A нельзя умножить на B")
        return []

    C = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            c = 0
            for k in range(len(A[0])):
                c += A[i][k] * B[k][j]
                C[i][j] = c
    return C


A = []
B = []

maxelementA = 0
maxelementB = 0

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
    sel = int(input())
    
    match sel:
        case 0:
            break
        case 1:
            aorb = matrix_select()
            print(f"Введите числа m{aorb} и n{aorb} через строку")
            if aorb == "A":
                mA = int(input())
                nA = int(input())
                if mA <= 0 or nA <= 0:
                    print("Числа, равные количествам строк и столбцов, должны быть > 0")
                    mA, nA = 0, 0
                    continue
                A = matrix_input(mA, nA, 1)
                print("Введена матрица A")
            elif aorb == "B":
                mB = int(input())
                nB = int(input())
                if mB <= 0 or nB <= 0:
                    print("Числа, равные количествам строк и столбцов, должны быть > 0")
                    mB, nB = 0, 0
                    continue
                B = matrix_input(mB, nB, 1)
                print("Введена матрица B")
        case 2:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                if aorb == "A":
                    matrix_output(A, mA, nA, len(str(maxelementA)))
                elif aorb == "B":
                    matrix_output(B, mB, nB, len(str(maxelementB)))
            else:
                print(f"Матрица {aorb} пустая или не является прямоугольной")
                
        case 3:
            if matrix_validity(A) and matrix_validity(B):
                if len(A) == len(B) and len(A[0]) == len(B[0]):
                    C = add_matrices(A, B)
                    maxelementC = findmax_element(C)
                    print("A + B =")
                    matrix_output(C, len(C), len(C[0]), len(str(maxelementC)))
                else:
                    print("Размеры матриц A и B не совпадают")
            else:
                print("Ни одна из матриц A и B не должна быть пустой или иметь пустые \"ячейки\"")
        case 4:
            if matrix_validity(A) and matrix_validity(B):
                if len(A) == len(B) and len(A[0]) == len(B[0]):
                    C = subtract_matrices(A, B)
                    maxelementC = findmax_element(C)
                    print("A - B =")
                    matrix_output(C, len(C), len(C[0]), len(str(maxelementC)))
                else:
                    print("Размеры матриц A и B не совпадают")
            else:
                print("Матрица A или B пустая или не прямоугольная")
        case 5:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                print("Введите скаляр")
                k = int(input())
                if aorb == "A":
                    print("k * A =")
                    C = multiply_by_scalar(A, k)
                elif aorb == "B":
                    print("k * B =")
                    C = multiply_by_scalar(B, k)
                lmeC = len(str(findmax_matrix(C)))
                matrix_output(C, len(C), len(C[0]), lmeC)
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
        case 6:
            aorb = matrix_select()
            if matrix_validity(A if aorb == "A" else B):
                if aorb == "A":
                    C = transpose(A)
                elif aorb == "B":
                    C = transpose(B)
                lmeC = len(str(findmax_matrix(C)))
                matrix_output(C, len(C), len(C[0]), lmeC)
            else:
                print(f"Матрица {aorb} пустая или не прямоугольная")
        case 7:
            if matrix_validity(A) and matrix_validity(B): 
                C = multiply_matrices(A, B)
                if C != []:
                    lmeC = len(str(findmax_matrix(C)))
                    matrix_output(C, len(C), len(C[0]), lmeC)
            else:
                print("Матрица A или B пустая или не прямоугольная")
#        case 8:
            #aorb = matrix_select()
            #if matrix



# не вся логика в мэйне
# все операции в отдельной функции
# меню должно работать в цикле до выбора 0
# некорректный номер пункта не завершает программу
# ошибки обрабатываются без аварийного завершения
# перед каждой операцией проверяются условия применимости
# результаты вычислений выводятся в удобном табличном формате
# вычислительные функции по возможности не содержат input() и print(), ввод/вывод рекомендуется разделить
