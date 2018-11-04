import numpy as np

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

A = np.matrix([[4,-1,1],[-1,3,0],[1,0,2]])
B = np.matrix([[4,1,1,1],[1,3,-1,1],[1,-1,2,0],[1,1,0,2]])

for i in [A,B]:
    L = Cholesky(i)
    LT = np.transpose(L)
    
    print("A =" + str(i) + " = ")
    print(L)
    print()
    print(str(LT) + " = LL*")
    print("-------------------------------------------------------------")
