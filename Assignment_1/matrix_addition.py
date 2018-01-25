import numpy as np
import matplotlib.pyplot as plt
import time

def rand_matrix(n,m):
    # random matrix of shape n x m
    # n: number of rows
    # m: number of columns

    matrix = np.matrix(np.random.random_integers(0,100, (n,m)))
    return matrix
    
def m_add(matrix_1, matrix_2):
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

trials = [100, 200, 300, 500, 1000]
matrices_A = []
matrices_B = []

for i,n in enumerate(trials):
    matrices_A.append(rand_matrix(n,n))
    matrices_B.append(rand_matrix(n,n))

def take_time(matrix1, matrix2, native):
    if native == True:
        start_time = time.time()
        matrix1 + matrix2
        result = time.time() - start_time
    else:
        start_time = time.time()
        m_add(matrix1, matrix2)
        result = time.time() - start_time

    return result
        
my_times = []
native_times = []

for i in range(len(trials)): # Bad but what the heck, who cares
    my_times.append(take_time(matrices_A[i], matrices_B[i], False))
    native_times.append(take_time(matrices_A[i], matrices_B[i], True))


plt.scatter(trials, my_times)
plt.scatter(trials, native_times)
plt.xlabel("Trials")
plt.ylabel("Time")
plt.title("Time vs Trials Matrix Addition")
plt.show()
    
    
