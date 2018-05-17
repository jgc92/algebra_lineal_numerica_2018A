import numpy as np

def Power(A:np.array ,x=None,N=25,tol=1e-10) -> (float,np.array):
    """ Power iteration method to find the aproximation to the greatest (in absulute value) eigenvalue of A. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            x: Guess vector.
            N: Maximum number of iterations.
            tol: Tolerance

        Returns:
            micra: Aproximation to the greatest eigenvalue (in absolute value)
            x: Aproximation to the eigenvector of micra.
    """

    if x is None:
        x = np.random.rand(A.shape[0])

    for i in range(N):
        x_new = np.dot(A,x)
        x_new_norm = np.linalg.norm(x_new ,np.inf)

        if np.allclose(x, (x_new/x_new_norm), rtol=tol):
            print('Itr:', i)
            break

        x = x_new / x_new_norm
        micra = np.dot(x, np.dot(A,x)) / np.dot(x,x)

    return micra, x

def InversePower(A,x=None,N=25,tol=1e-10) -> (float,np.array):
    """ Inverse Power iteration method to find the aproximation to the greatest (in absulute value) eigenvalue of A. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            x: Guess vector.
            N: Maximum number of iterations.
            tol: Tolerance

        Returns:
            micra: Aproximation to the greatest eigenvalue (in absolute value)
            x: Aproximation to the eigenvector of micra.
    """
        
    if x is None:
        x = np.random.rand(A.shape[0])
        
    micra = np.dot(x, np.dot(A,x)) / np.dot(x,x)
    
    for i in range(N):
        try:
            x_new = np.linalg.solve((A - micra * np.eye(A.shape[0])),x)
        except np.linalg.LinAlgError as err:
            if 'Singular matrix' in str(err):
                print('A es singular')
                return micra, x
            else:
                raise

        x_new_norm = np.linalg.norm(x_new ,np.inf)

        if np.allclose(x, (x_new/x_new_norm), rtol=tol):
            print('Itr:', i)
            break

        x = x_new / x_new_norm
        micra = np.dot(x, np.dot(A,x)) / np.dot(x,x)

    return micra, x

# For testing
#sol = InversePower(np.array([[2,2,3], [1, 4,1],[1,9,2]]), N=100)
#print(sol)

