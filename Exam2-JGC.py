import numpy as np
import matplotlib.pyplot as plt

def SOR(A:np.array, b:np.array,w:float ,x=None,N=25) -> np.array:
    m,n = len(A[0]),len(A[1])
    
    if x is None:
        x = np.zeros(m)

    D = np.diagflat(np.diag(A))
    L = np.tril(A,-1)
    U = np.triu(A,1)

    for i in range(N):
        prev_x = x
        x = np.dot(np.linalg.inv(D + w*L),(w*b - np.dot((w*U + (w-1)*D),x)))
    return x

A = np.array([[3,-1,0,0,0,1/2],
              [-1,3,-1,0,1/2,0],
              [0,-1,3,-1,0,0],
              [0,0,-1,3,-1,0],
              [0,1/2,0,-1,3,-1],
              [1/2,0,0,0,-1,3]])

b = np.array([5/2,3/2,1,1,3/2,5/2])
guess = b / np.diagonal(A)
u = np.array([1,1,1,1,1,1])

ws = np.arange(1,1.3,0.01)
sols = []
errs = []

for i,w in enumerate(ws):
    sols.append(SOR(A,b,w,guess,10))
    errs.append(np.linalg.norm(u - sols[i]))

plt.plot(ws,errs)
plt.show()


