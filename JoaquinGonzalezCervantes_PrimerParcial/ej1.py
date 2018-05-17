import numpy as np

def Frobenius(A):
    A = np.matrix(A)
    rows, cols = A.shape
    result = 0

    for i in range(rows):
        for j in range(cols):
            result += np.abs(A[i,j])**2


    print(np.sqrt(result))
    return np.sqrt(result)

A = [-3,4,1,4],[-6,9,5,-3],[3,-1,8,2]
Frobenius(A)



