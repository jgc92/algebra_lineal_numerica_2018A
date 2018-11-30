import numpy as np

def jacobi(A,b,x=None,N=25,tol=1e-10):
    m = len(A[0])

    if x is None:
        x = np.zeros(m)

    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(N):
        prev_x = x
        x = (b - np.dot(R, x)) / D
        if np.allclose(x, prev_x, rtol=tol):
            print('Itr:', i)
            break
    return x

def Tj(A):
    D = np.diagflat(np.diag(A))
    L = np.tril(-A,-1)
    U = np.triu(-A,1)

    return np.dot(np.linalg.inv(D), L + U)

def Tg(A):
    D = np.diagflat(np.diag(A))
    L = np.tril(-A,-1)
    U = np.triu(-A,1)

    return np.dot(np.linalg.inv(D-L),U)


def SOR(A,b,w,x=None,N=25,tol=1e-10):
    m = len(A[0])

    if x is None:
        x = np.zeros(m)

    D = np.diagflat(np.diag(A))
    L = np.tril(A,-1)
    U = np.triu(A,1)

    for i in range(N):
        prev_x = x
        x = np.dot(np.linalg.inv(D + w*L),(w*b - np.dot((w*U + (w-1)*D),x)))
        if np.allclose(x, prev_x, rtol=tol):
            print('Itr:', i)
            break
    return x

def gSeidel(A,b,x=None,N=25,tol=1e-10):
    return SOR(A,b,1,x,N,tol)

def cg(A,b,x=None,N=25, tol=1e-10):
    m = len(A[0])

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


#A = np.array([[3,-1,1],[3,6,2],[3,3,7]])
#b = np.array([1,0,4])
#x = np.array([1/3,0,4/7])

#A = np.array([[10,-1,0],[-1,10,-2],[0,-2,10]])
#b = np.array([9,7,6])
#x = np.array([9/10,7/10,6/10])

#A = np.array([[10,5,0,0],[5,10,-4,0],[0,-4,8,-1],[0,0,-1,5]])
#b = np.array([6,25,-11,-11])
#x = np.array(np.round([6/10,25/10,-11/8,-11/5],5))
#print(SOR(A,b,1,x,1000,tol=1e-5))

#A = np.array([[1,2,-2],[1,1,1],[2,2,1]])
#b = np.array([7,2,5])

A = np.array([[2,-1,1],[2,2,2],[-1,-1,2]])
b = np.array([-1,4,-5])
x = np.array([-1/2,4/2,-5/2])

print(jacobi(A,b,x,1000,tol=1e-5))

#vals, vecs = np.linalg.eig(Tg(A))
#print(np.amax(np.abs(vals)))
