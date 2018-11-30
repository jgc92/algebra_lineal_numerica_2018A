import numpy as np

def rayleigh(A,v):
    return (v.T @ A @ v)/(v.T @ v)

def Power(A,x=None,N=25,tol=1e-10):
    if x is None:
        x = np.random.rand(A.shape[0])

    for i in range(N):
        x_new = np.dot(A,x)
        x_new_norm = np.linalg.norm(x_new ,np.inf)

        if np.allclose(x, (x_new/x_new_norm), rtol=tol):
            print('Itr:', i)
            break

        x = x_new / x_new_norm
        lam = rayleigh(A,x)

    print('Itr:', N)
    return x, lam

def InversePower(A,x=None,N=25,tol=1e-10):
    if x is None:
        x = np.random.rand(A.shape[0])

    micra = np.dot(x, np.dot(A,x)) / np.dot(x,x)

    for i in range(N):
        x_new = np.linalg.solve((A - micra * np.eye(A.shape[0])),x)

        x_new_norm = np.linalg.norm(x_new ,np.inf)

        if np.allclose(x, (x_new/x_new_norm), rtol=tol):
            print('Itr:', i)
            break

        x = x_new / x_new_norm
        micra = np.dot(x, np.dot(A,x)) / np.dot(x,x)
        lam = rayleigh(A,x)


    print("Itrs", N)
    return x, lam

A = np.array([[2,1,1],[1,2,1],[1,1,2]])
x = np.array([1,-1,2])
B = np.array([[1,-1,0],[-2,4,-2],[0,-1,2]])
y = np.array([-1,2,1])

print(Power(A,x,5))
print(Power(B,y,5))
print(InversePower(B,y,5))
