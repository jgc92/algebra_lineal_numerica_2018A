import numpy as np

def T_matrix(n):
    if n < 3:
        return "invalid n"
    else:
        T = np.zeros((n,n))
        np.fill_diagonal(T, np.full(n,2))
        np.fill_diagonal(T[1:,:], np.full(n-1,-1))
        np.fill_diagonal(T[:,1:], np.full(n-1,-1))

        return T

def Frobenius(A):
    A = np.matrix(A)
    rows, cols = A.shape
    result = 0

    for i in range(rows):
        for j in range(cols):
            result += np.abs(A[i,j])**2

    return np.sqrt(result)

for i in [10,20,30]:
    T = T_matrix(i)
    print(Frobenius(T))


