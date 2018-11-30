import numpy as np
import matplotlib.pyplot as plt

def LUTridiagonal(A):
    A = np.matrix(A)
    m,n = A.shape
    d = np.squeeze(np.asarray(A.diagonal()))
    a = np.squeeze(np.asarray(A.diagonal(-1)))
    c = np.squeeze(np.asarray(A.diagonal(1)))

    l = np.zeros(n-1)
    v = np.zeros(n)

    v[0] = d[0]

    for i in range(1,n):
        l[i-1] = a[i-1] / v[i-1]
        v[i] = d[i] - np.dot(l[i-1],c[i-1])

    L = np.eye(m,n, dtype=int) + np.diag(l, -1)
    U = np.diag(v) + np.diag(c,1)

    return L,U

def SolveTridiagonal(A:np.array ,b:np.array) -> np.array:
    L,U = LUTridiagonal(A)
    d = np.squeeze(np.asarray(U.diagonal()))
    a = np.squeeze(np.asarray(L.diagonal(-1)))
    c = np.squeeze(np.asarray(U.diagonal(1)))

    n = len(d)
    x = np.zeros(n)
    x[0] = b[0]

    for i in range(1,n):
        x[i] = b[i] - a[i-1] * x[i-1]

    x[n-1] = x[n-1] / d[n-1]

    for i in range(n-2,-1,-1):
        x[i] = ( x[i] - c[i] * x[i+1] ) / d[i]

    return x

def tridiagonal(n,lam):
    T = np.zeros((n,n))
    np.fill_diagonal(T, (1+2*lam))
    np.fill_diagonal(T[1:,:], -lam)
    np.fill_diagonal(T[:,1:], -lam)

    return T

def tridiagdot(A,x):
    n = A.shape[0]
    p = A[0,0]
    s = A[0,1]

    pDiag = np.full(n,p)

    uDiag = np.full(n,s)
    uDiag[0] = 0

    lDiag = np.full(n,s)
    lDiag[-1] = 0

    return (pDiag + lDiag + uDiag) * x

def cg2(A,b,x=None,N=50, tol=1e-10):
    m = len(A[0])

    if x is None:
        x = np.zeros(m)

    r = b - tridiagdot(A,x)
    p = r
    rsold = np.dot(r,r)

    for i in range(N):
        Ap = tridiagdot(A, p)
        alpha = rsold / np.dot(p,Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r,r)

        if np.sqrt(rsnew) < tol:
            #print('Itr:', i)
            break

        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return x

def f(x):
    return (2*x-x**2)*np.sin(2*np.pi*x)

m = 9999 # WARNING: SolveTridiagonal may not handle this size.
h = 2/(m+1)
k = 0.01
alpha = 0.15

x=np.linspace(h,2-h,m)

lam = (alpha)**2*(k/h**2)

A = tridiagonal(m,lam)

for i in [0,1,200,300]:
    u0 = f(x)
    for _ in range(i):
        #u0 = SolveTridiagonal(A,u0)
        u0 = cg2(A,u0)

    print(u0)
    plt.plot(x,u0)

plt.show()
