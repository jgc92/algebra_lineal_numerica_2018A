import numpy as np
import matplotlib.pyplot as plt
import time

def rand_matrix(n,m):
    # random matrix of shape n x m
    # n: number of rows
    # m: number of columns

    matrix = np.matrix(np.random.random_integers(0,100, (n,m)))
    return matrix
    
def m_mult(matrix_1, matrix_2):
    # matrix_n is of type numpy.matrixlib.defmatrix.matrix
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

m1 = rand_matrix(2,3)
m2 = rand_matrix(3,5)

print(m_mult(m1,m2))
