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


A = [[3, 5],
     [2, 4]]

if len(A) != len(A[0]):
    raise Exception("матрица не квадратная")

print(determinant(A))

"""
> реализовать алгоритм поиска детерминанта матрицы n x n используя метод Гаусса или разложение по строке... numpy нельзя

зачем?
"""

