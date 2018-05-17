import numpy as np
    
def GramSchimdt(V:np.array) -> np.matrix:
    """ Gram Schimdt proccess to orthonormalize a set of vectors. Done in a hurry, expect bugs JGC.
        Args:
            V: A list representation of the vector to orthonormalize, or numpy type matrix.

        Returns:
            U: A matrix representation of the orthonormalized vectors.
    """

    V = np.matrix(V)
    m,n = V.shape
    U = np.zeros((m,n))

    U[:,0] = V[:,0].squeeze() / np.linalg.norm(V[:,0])

    for i in range(1,n):
        U[:,i] = V[:,i].squeeze()
        for j in range(i):
            proj = np.dot(( np.dot(U[:,i], U[:,j] )/( np.dot(U[:,j],U[:,j]) )), U[:,j])
            U[:,i] = U[:,i].squeeze() - proj
                          

        U[:,i] = U[:,i].squeeze() / np.linalg.norm(U[:,i])

    return U
