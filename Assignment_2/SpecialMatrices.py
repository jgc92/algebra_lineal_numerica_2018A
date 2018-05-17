import numpy as np

def LUTridiagonal(A:np.array) -> (np.matrix, np.matrix):
    """ LU decomposition for tridiagonal matrices. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.

        Returns:
            L: Lower triangular matrix.
            U: Upper triangular matrix.
    """
    
    A = np.matrix(A)
    m,n = A.shape
    d = np.squeeze(np.asarray(A.diagonal()))
    a = np.squeeze(np.asarray(A.diagonal(-1)))
    c = np.squeeze(np.asarray(A.diagonal(1)))

    l = np.zeros(n-1)
    v = np.zeros(n)

    v[0] = d[0]

    for i in range(1,n):
        l[i-1] = a[i-1] / v[i-1]
        v[i] = d[i] - np.dot(l[i-1],c[i-1])

    L = np.eye(m,n, dtype=int) + np.diag(l, -1)
    U = np.diag(v) + np.diag(c,1)

    return L,U

def SolveTridiagonal(A:np.array ,b:np.array) -> np.array:
    """ Solve system of equations with tridiagonal matrix representation. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            b: vector in Ax = b.

        Returns:
            x: Solution vector in Ax = b.
    """

    L,U = LUTridiagonal(A)
    d = np.squeeze(np.asarray(U.diagonal()))
    a = np.squeeze(np.asarray(L.diagonal(-1)))
    c = np.squeeze(np.asarray(U.diagonal(1)))

    n = len(d)
    x = np.zeros(n)
    x[0] = b[0]
    
    for i in range(1,n):
        x[i] = b[i] - a[i-1] * x[i-1]

    x[n-1] = x[n-1] / d[n-1]

    for i in range(n-2,-1,-1):
        x[i] = ( x[i] - c[i] * x[i+1] ) / d[i]

    return x

# For testing
#A = np.matrix([[1,4,0,0],[3,4,1,0],[0,2,3,4],[0,0,1,3]])
#b = np.array([1,3,4,0])

#x = SolveTridiagonal(A,b)
#print(x)


