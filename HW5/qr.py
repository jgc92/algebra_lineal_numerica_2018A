import numpy as np
    
def GramSchmidt(A):
    A = np.matrix(A)
    m,n = A.shape
    v = np.zeros((m,n))
    q = np.zeros((m,n))

    for i in range(n):
        v[:,i] = A[:,i].squeeze()
    for i in range(n):
        r = np.linalg.norm(v[:,i])
        q[:,i] = v[:,i].squeeze() / r
        for j in range(i+1,n):
            rr = q[:,i]@v[:,j]
            v[:,j] = v[:,j] - rr*q[:,i]

    return q

def GramSchmidtUnstable(A):
    A = np.matrix(A)
    m,n = A.shape
    v = np.zeros((m,n))
    q = np.zeros((m,n))
    
    for j in range(n):
        v[:,j] = A[:,j].squeeze()
        rr = np.linalg.norm(v[:,j])
        q[:,j] = v[:,j].squeeze() / rr

        for i in range(1,j):
            r = q[:,i]@A[:,j]
            v[:,j] = v[:,j] - r*q[:,i]

    return q
    
def QRGramSchmidt(A):
    A = np.array(A)
    m,n = A.shape
    R = np.zeros((m,n))
    Q = np.array(GramSchmidt(A))

    for i in range(n):
        for j in range(n):
            R[i,j] = A[:,j]@Q[:,i]

    R = np.triu(R)

    return Q,R

A = np.matrix([[1,0],[0,1],[1,0]])
B = np.matrix([[1,2],[0,1],[1,0]])
C = np.matrix([[4,-2,3],[1,2,6],[8,5,1],[-5,8,-5]])

AA = np.matrix([[1.2969, 0.8648],[0.2161, 0.1441]])

print(QRGramSchmidt(A))
print(QRGramSchmidt(B))
print(QRGramSchmidt(C))
print(QRGramSchmidt(AA))




