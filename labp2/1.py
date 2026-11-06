def matrix_input(m, n):
    global maxelement

    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        try:
            row = list(map(int, input().split()))
        except ValueError:
            print("В строке должны быть только целые числа")
            exit(1)

        if len(row) != n:
            raise ValueError(f"В строке должно быть {n} элементов")

        matrix[i] = row

        for j in range(n):
            if matrix[i][j] > maxelement:
                maxelement = matrix[i][j]

    return matrix


def matrix_output(matrix, m, n, cellwidth):
    for i in range(m):
        for j in range(n):
            print(str(matrix[i][j]).ljust(cellwidth, " "), end=" ")
        print()      


m = int(input())
n = int(input())

if m <= 0 or n <= 0:
    raise ValueError("Числа, равные количествам строк и столбцов, должны быть > 0")

maxelement = 0
matrix = matrix_input(m, n)
lme = len(str(maxelement))

print(matrix)
matrix_output(matrix, m, n, lme)
