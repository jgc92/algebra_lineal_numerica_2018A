import numpy as np

def qrH(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        a = A[i:, i]
        H[i:, i:] = houseHolder(a.reshape((len(a),1)))
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A

def houseHolder(a):
    m,n = a.shape
    v = np.copy(a)
    v = v + np.copysign(np.linalg.norm(a), a[0,0]) * np.eye(m,n)
    v = v/np.linalg.norm(v)

    H = np.eye(a.shape[0]) - 2 * np.outer(v, v.T)
    return H


def qrG(A):
    m,n = np.shape(A)
    Q = np.identity(m)
    R = np.copy(A)

    rows, cols = np.tril_indices(m, -1, n)
    for (row, col) in zip(rows, cols):
        if R[row, col] != 0:
            c, s = givensCoeffs(R[col, col], R[row, col])

            G = np.eye(m)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s

            R = np.dot(G, R)
            Q = np.dot(Q, G.T)
    return Q, R


def givensCoeffs(a, b):
    r = np.hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)

def triH(A):
    for i in np.arange(A.shape[0] - 2):
        H = np.eye(A.shape[0])
        H[i+1:,i+1:] = houseHolder(A[i+1:,i].reshape((len(A[i+1:,i]),1)))
        A = H @ A @ H
    return A.round(6)

A = np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
print(triH(A))
