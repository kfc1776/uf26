def main_diagonal(matrix):
    d = []
    for i in range(len(matrix)):
        d.append(matrix[i][i])
    return d


def secondary_diagonal(matrix):
    d = []
    for i in range(len(matrix)):
        d.append(matrix[i][len(matrix)-1-i])
    return d


def trace(matrix):
    return (sum(main_diagonal(matrix)),
            sum(secondary_diagonal(matrix)))


matrix = [[1, 2, 1],
          [4, 5, 6],
          [7, 8, 9]]

if len(matrix) != len(matrix[0]):
    raise Exception("матрица не квадратная")

ms, ss = trace(matrix)

print("Main diagonal:", main_diagonal(matrix))
print("Sum:", ms)
print("Secondary diagonal:", secondary_diagonal(matrix))
print("Sum:", ss)
