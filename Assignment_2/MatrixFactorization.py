import numpy as np
from copy import copy
from DirectSolvers import *

def LUGauss(M: list) -> (np.matrix):
    """ LU decompositions using Gaussian Elimination without pivoting. Done in a hurry, expect bugs JGC.
        Args:
            M: A list representation of a matrix.

        Returns:
            L and U decompositions in M = LU.
    """

    M = np.matrix(M, dtype=np.float)
    rows, cols = M.shape

    # Gaussian Elimination no pivoting
    # Get multipliers
    U, multi_matrix = GE(M,multipliers=True)

    # Construct L
    L = np.matrix(np.tril(multi_matrix))

    return L, U

def LUDoolittle(M: list) -> (np.matrix):
    """ LU decompositions using Doolittle's method. Done in a hurry, expect bugs JGC.
        Args:
            M: A list representation of a matrix.

        Returns:
            L and U decompositions in M = LU.
    """
    M = np.matrix(M, dtype=np.float)
    rows, cols = M.shape


    # Create zero matrices for L and U
    L = np.matrix(np.zeros((rows,cols)))
    U = np.matrix(np.zeros((rows,cols)))

    for j in range(cols):
        for i in range(j + 1):
            # Better way to do the sums
            acc1 = sum(U[k,j] * L[i,k] for k in range(i))
            U[i,j] = M[i,j] - acc1

        for i in range(j, rows):
            # Better way to do the sums
            acc2 = sum(U[k,j] * L[i,k] for k in range(j))
            L[i,j] = (M[i,j] - acc2) / U[j,j]

    return L,U

def Cholesky(M: list) -> (np.matrix):
    """ LL* or Cholesky decomposition. Done in a hurry, expect bugs JGC.
        Args:
            M: A list representation of a matrix.

        Returns:
            L decompositions in M = LL*.
    """
    M = np.matrix(M, dtype=np.float)
    rows, cols = M.shape

    # Initialize matrix with zeros
    L = np.zeros((rows,cols))

    # First component
    L[0,0] = np.matrix(np.sqrt(M[0,0]))

    # First column
    for i in range(1, rows):
        L[i,0] = 1 / float(L[0,0]) * M[i,0]

    
    for i in range(rows):
        acc = sum(L[i,j] ** 2 for j in range(i))

        # The diagonal other than the first component
        L[i,i] = np.sqrt(M[i,i] - acc)

        # Break loop
        if i + 1 == rows:
            return L

        # Below the diagonal other than the first column
        acc = 0
        for k in range(i):
            if k == 0:
                acc = L[i + 1,k] * L[i,k]
            else:
                acc = acc - L[i + 1,k] * L[i,k]

        L[i + 1,i] = 1 / float(L[i,i]) * (M[i + 1,i] - acc)

    return L



# For testing
#A = [[4,12,-16],[12,37,-43],[-16,-43,98]]
#print(Cholesky(A))

#A = [[1,1,1],[2,-3,1],[-1,2,-1]]
#b = [4,2,-1]
#x,y = GE(A,True,True)
#print(y)
#print(GaussSimple(A,b))
#print(LUGauss(A))

    


