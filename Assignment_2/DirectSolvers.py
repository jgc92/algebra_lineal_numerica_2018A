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

    # Gaussian Elimination
    for j in range(cols-1):
        if pivoting:
            #Choose largest pivot element below (and including) j
            maxindex = abs(M[j:,j]).argmax() + j
            if M[maxindex, j] == 0:
                print("Matrix is singular.")
            #Swap rows
            if maxindex != j:
                M[[j,maxindex]] = copy(M[[maxindex, j]])
                
        for i in range(j,rows-1):
            multi = M[i+1,j] / M[j,j]
            
            # Collect multipliers
            multi_matrix[i+1,j] = multi

            M[i+1,:] = M[i+1,:] - (multi * M[j,:])

    if multipliers:
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
    
    # Back substitution
    x = BASUB(UT)

    if verbose:
        print(UT)

    return np.flip(x,0)
    

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

    return np.flip(x,0)


def GaussJordan(A: list ,b: list ,verbose=False) -> np.matrix:
    """ Solve Ax=b using Gauss-Jordan. Done in a hurry, expect bugs JGC.
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
    rows, cols = M.shape

    # Gaussian Elimination, no pivoting
    UT = GE(M)

    # Backward Gaussian Elimination, no pivoting
    for j in range(cols-2,-1,-1):
        for i in range(j,0,-1):
            multi = UT[i-1,j] / UT[j,j]

            UT[i-1,:] = UT[i-1,:] - (multi * UT[j,:])

    # Back substitution
    x = BASUB(UT)
    
    if verbose:
        print(UT)

    return x

# For testing
#A = [[1,1,1],[2,-3,1],[-1,2,-1]]
#b = [4,2,-1]
#x,y = GE(A,True,True)
#print(y)
#print(GaussSimple(A,b))
