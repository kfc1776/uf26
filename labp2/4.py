def transpose(matrix):
    B = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for j in range(len(B)):
        for i in range(len(B[0])):
            B[j][i] = matrix[i][j]
    return B

A = [[1, 2, 3],
     [4, 5, 6]]

for i in transpose(A):
    print(*i)
