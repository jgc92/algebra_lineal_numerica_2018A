import numpy as np
import time

def m_mult(matrix_1: np.matrix, matrix_2: np.matrix) -> np.matrix:
    """ Performs matrix multiplication.

        Args:
            matrix_1
            matrix_2

        Returns:
            Matrix multiplication.
    """
    
    m1_shape = matrix_1.shape
    m2_shape = matrix_2.shape
    rows = m1_shape[0]
    columns = m1_shape[1]

    result = np.matrix(np.zeros((m1_shape[0],m2_shape[1])))

    if m1_shape[1] != m2_shape[0]:
        print("This matrices cannot be multiplied, they have incopatible shapes!!!!")
        return
    else:
        for i in range(m1_shape[0]):
            for j in range(m2_shape[1]):
                for k in range(m2_shape[0]):
                    result[i,j] += matrix_1[i,k] * matrix_2[k,j]
                
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
        matrix1 * matrix2
        result = time.time() - start_time
    else:
        start_time = time.time()
        m_mult(matrix1, matrix2)
        result = time.time() - start_time

    return result
