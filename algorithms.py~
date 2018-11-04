import numpy as np
from copy import copy

def GE(M: list, pivoting=True, multipliers=False) -> np.matrix:
    """ Gaussian Elimiation with optional partial pivoting. Done in a hurry, expect bugs JGC.
        Args:
            M: A list representation of a matrix.
            pivotiong: Bool. Enable or disable partial pivoting.
            multipliers: Bool. Return list with multipliers for use in decompositions.

        Returns:
            Gaussian Elimination of M. Optional list of multipliers.
    """

    M = np.matrix(M, dtype=np.float)
    rows, cols = M.shape
    # Initialize multipliers matrix
    multi_matrix = np.matrix(np.ones((rows,cols)))
    P = np.eye(rows)

    # Gaussian Elimination
    for j in range(cols-1):
        if pivoting:
            # Initialize permutation matrix
            PP = np.eye(rows)
    
            #Choose largest pivot element below (and including) j
            maxindex = np.abs(M[j:,j]).argmax() + j

            if M[maxindex, j] == 0:
                print("Matrix is singular.")
            #Swap rows
            if maxindex != j:
                M[[j,maxindex]] = copy(M[[maxindex, j]])
                PP[[j,maxindex]] = copy(PP[[maxindex, j]])

                P = np.dot(PP,P)
                
                
        for i in range(j,rows-1):
            if M[j,j] == 0:
                return False
                
            multi = M[i+1,j] / M[j,j]

            if pivoting and maxindex != j:
                multi_matrix = np.dot(PP,multi_matrix)

            # Collect multipliers
            multi_matrix[i+1,j] = multi


            M[i+1,:] = M[i+1,:] - (multi * M[j,:])

    if multipliers and pivoting:
        return M, multi_matrix, P
    elif multipliers:
        return M, multi_matrix
    else:
        return M

def BASUB(T: list) -> np.matrix:
    """ Back substitution for an upper triangular matrix. Done in a hurry, expect bugs JGC.
        Args:
            T: A list representation of a upper triangular matrix.

        Returns:
            x in Ax=b.
    """
    
    M = np.matrix(T, dtype=np.float)
    rows, cols = M.shape
    x = np.zeros(rows)

    # Check if upper triangular
    if np.allclose(M, np.triu(M)):
        # Substitution
        for i in range(rows-1,-1,-1):
            x[i] = M[i,rows] / M[i,i]
            for k in range(i-1,-1,-1):
                M[k,rows] -= M[k,i] * x[i]
    else:
        print('BASUB error: Not Upper Triangular Matrix')

    return x

def GaussSimple(A: list ,b: list,verbose=False) -> np.matrix:
    """ Solve Ax=b using Gaussian Elimination without pivoting. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix.
            b: A list representation of a vector.
            verbose: Bool (optional). For exam purposes.

        Returns:
            x in Ax=b.
    """
    
    A = np.matrix(A, dtype=np.float)
    b = np.matrix(b, dtype=np.float)

    # Augmented matrix
    M = np.concatenate((A,b.transpose()),1)

    # Gaussian Elimination, no pivoting
    UT = GE(M, pivoting=False)

    if UT == False:
        print("Gauss Simple failed: zero in pivot")
        return 
    
    # Back substitution
    x = BASUB(UT)

    if verbose:
        print(UT)

    return x
    

def GaussPartialPivoting(A: list ,b: list, verbose=False ) -> np.matrix:
    """ Solve Ax=b using Gaussian Elimination with partial pivoting. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix.
            b: A list representation of a vector.
            verbose: Bool (optional). For exam purposes.

        Returns:
            x in Ax=b.
    """

    A = np.matrix(A, dtype=np.float)
    b = np.matrix(b, dtype=np.float)

    # Augmented matrix
    M = np.concatenate((A,b.transpose()),1)

    # Gaussian elimination with partial pivoting
    UT = GE(M)

    # Back substitution
    x = BASUB(UT)

    if verbose:
        print(UT)

    return x


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
    U, multi_matrix = GE(M,pivoting=False,multipliers=True)

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

def PLUGauss(M: list) -> (np.matrix):
    """PA = LU decompositions using Gaussian Elimination with pivoting. Done in a hurry, expect bugs JGC.
        Args:
            M: A list representation of a matrix.

        Returns:
            P,L and U decompositions in PM = LU.
    """

    M = np.matrix(M, dtype=np.float)
    rows, cols = M.shape

    # Gaussian Elimination no pivoting
    # Get multipliers
    U, multi_matrix, P = GE(M,pivoting=True,multipliers=True)

    # Construct L
    L = np.matrix(np.tril(multi_matrix))

    return L, U, P
