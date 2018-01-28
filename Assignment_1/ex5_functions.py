import numpy as np
import time

def rand_matrix(n: int ,m: int) -> np.matrix:
    """ Returns random numpy matrix of shape n x m.

        Args:
            n: number of rows.
            m: number of columns.

        Return:
            Random numpy matrix type of shape n x m
    """

    matrix = np.matrix(np.random.random_integers(0,100, (n,m)))
    return matrix
    
def m_add(matrix_1: np.matrix, matrix_2: np.matrix) -> np.matrix:
    """ Performs matrix addition between two matrices.

        Args:
            matrix_1
            matrix_2

        Return:
            Matrix addition of matrix_1 and matrix_2.
    """

    # matrix_n is of type numpy.matrixlib.defmatrix.matrix
    m1_shape = matrix_1.shape
    m2_shape = matrix_2.shape
    rows = m1_shape[0]
    columns = m1_shape[1]

    result = np.matrix(np.zeros((rows,columns)))

    if m1_shape != m2_shape:
        print("This matrices cannot be added, they have different shapes!!!!")
        return
    else:
        for i in range(columns):
            for j in range(rows):
                result[i,j] = matrix_1[i,j] + matrix_2[i,j]
                
    return result

def take_time(matrix1: np.matrix, matrix2: np.matrix, native=False) -> float:
    """ Measures matrix addition time execution. If native = True uses native addition
        otherwise uses m_add matrix addition.

        Args:
            matrix_1
            matrix_2
            native: True for native addition, False for m_add addition.

        Return:
            Execution time in seconds.
    """
    if native == True:
        start_time = time.time()
        matrix1 + matrix2
        result = time.time() - start_time
    else:
        start_time = time.time()
        m_add(matrix1, matrix2)
        result = time.time() - start_time

    return result
