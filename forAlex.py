import numpy as np

def GramSchimdt(V):
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

def qrChafa(A):
    A = np.matrix(A)
    m,n = A.shape
    R = np.zeros((m,n))
    Q = GramSchimdt(A)

    for i in range(m):
        for j in range(n):
            R[i,j] = np.dot(Q[:,i],A[:,j])

    R = np.triu(R)

    return Q,R

def qrMethod(A,k):
    vals = np.zeros(A.shape[0])
    for i in range(k):
        Q,R = qrChafa(A)
        A = R @ Q

        if np.allclose(A.diagonal(), vals):
            print('Iterations:' + str(i))
            return A
        vals = A.diagonal()

    print('Iterations:' + str(k))
    return A



A = np.array([[1,3,4],[3,1,2],[4,2,1]])
qrMethod(A,20)
