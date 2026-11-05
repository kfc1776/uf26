def determinant(matrix):
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


def get_minor(matrix, row, col):
    return [
        [k for j, k in enumerate(r) if j != col]
        for i, r in enumerate(matrix) if i != row
    ]     

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

if len(A) != len(A[0]):
    raise Exception("матрица не квадратная")

minor = get_minor(A, 1, 1)

for i in minor:
    print(*i)

print(determinant(minor))
