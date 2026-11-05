def transpose(matrix):
    return [
            [matrix[i][j] for i in range(len(matrix))]
             for j in range(len(matrix[0]))
             ]


A = [[1,2,3],
     [4,5,6]]

if A == [] or not any(A):
    raise Exception("матрица пустая. так нельзя.")

for i in range(1, len(A)):
    if len(A[i]) != len(A[0]):
        raise Exception("матрица немного не прямоугольная.")

min_A = A[0][0]
max_A = A[0][0]
sum_A = 0

row_sums_A = []
col_sums_A = []

for i in range(len(A)):
    for j in range(len(A[0])):
        min_A = A[i][j] if A[i][j] < min_A else min_A
        max_A = A[i][j] if A[i][j] > max_A else max_A
        sum_A += A[i][j]
    row_sums_A.append(sum(A[i]))

A_T = transpose(A)

for i in range(len(A_T)):
    col_sums_A.append(sum(A_T[i]))

print(f"Размер: {len(A)} x {len(A[0])}")
print("Минимальный элемент:", min_A)
print("Максимальный элемент:", max_A)
print("Сумма элементов:", sum_A)
print("Среднее значение:", sum_A / (len(A) * len(A[0])))
print()
print("Суммы строк:", ', '.join(map(str, row_sums_A)))
print("Суммы столбцов:", ', '.join(map(str, col_sums_A)))

