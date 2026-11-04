def scalar_multiplication(matrix, scalar):
    B = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = matrix[i][j] * scalar
    return B

A = [[1, 2],
     [3, 4]]
k = 3

for i in scalar_multiplication(A, k):
    print(*i)
