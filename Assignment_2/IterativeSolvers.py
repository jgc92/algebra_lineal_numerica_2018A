import numpy as np

def Jacobi(A:np.array, b:np.array ,x=None,N=25,tol=1e-10) -> np.array:
    """ Jacobi iterative method for aproximation to the solution to Ax = b. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            b: b vector in Ax = b.
            x: Guess vector.
            N: Maximum number of iterations.
            tol: Tolerance

        Returns:
            x: Aproximation to the solution to Ax = b.
    """

    m,n = len(A[0]),len(A[1])
    
    # Create an initial guess if needed    
    if x is None:
        x = np.zeros(m)

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iterate for N times
    for i in range(N):
        prev_x = x
        x = (b - np.dot(R, x)) / D
        if np.allclose(x, prev_x, rtol=tol):
            print('Itr:', i)
            break
    return x


def SOR(A:np.array, b:np.array,w:float ,x=None,N=25,tol=1e-10) -> np.array:
    """ SOR iterative method for aproximation to the solution to Ax = b. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            b: b vector in Ax = b.
            x: Guess vector.
            w: weight
            N: Maximum number of iterations.
            tol: Tolerance

        Returns:
            x: Aproximation to the solution to Ax = b.
    """

    m,n = len(A[0]),len(A[1])
    
    # Create an initial guess if needed    
    if x is None:
        x = np.zeros(m)

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    #D = np.diagflat(np.diag(A))
    D = np.diagflat(np.diag(A))
    L = np.tril(A,-1)
    U = np.triu(A,1)

    # Iterate for N times
    for i in range(N):
        prev_x = x
        x = np.dot(np.linalg.inv(D + w*L),(w*b - np.dot((w*U + (w-1)*D),x)))
        if np.allclose(x, prev_x, rtol=tol):
            print('Itr:', i)
            break
    return x

def GaussSeidel(A:np.array, b:np.array,x=None,N=25,tol=1e-10) -> np.array:
    """ Gauss-Seidel iterative method for aproximation to the solution to Ax = b. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            b: b vector in Ax = b.
            x: Guess vector.
            N: Maximum number of iterations.
            tol: Tolerance

        Returns:
            x: Aproximation to the solution to Ax = b.
    """

    return SOR(A,b,1,x,N,tol)

def ConjugateGradient(A:np.array, b:np.array, x=None, N=25, tol=1e-10) -> np.array:
    """ Conjugate Gradient iterative method for aproximation to the solution to Ax = b. Done in a hurry, expect bugs JGC.
        Args:
            A: A list representation of a matrix, or numpy type matrix.
            b: b vector in Ax = b.
            x: Guess vector.
            N: Maximum number of iterations.
            tol: Tolerance

        Returns:
            x: Aproximation to the solution to Ax = b.
    """

    m,n = len(A[0]),len(A[1])
    
    if x is None:
        x = np.zeros(m)
        
    r = b - np.dot(A,x)
    p = r
    rsold = np.dot(r,r)
    
    for i in range(N):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p,Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r,r)
        
        if np.sqrt(rsnew) < tol:
            print('Itr:', i)
            break
        
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return x

#For testing

#A = np.array([[16,3],[7,-11]])
#b = np.array([11,13])
#guess = np.array([1.0,1.0])

#sol = jacobi(A,b,x=None,N=25,tol=1e-20)
#sol = SOR(A,b,1,None,100,1e-20)
#sol = GaussSeidel(A,b,None,100)
#sol = conjugate_grad(A,b,None,100)

#print(sol)




