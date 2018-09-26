import numpy as np
import matplotlib.pyplot as plt
from algorithms import *

def fie(a,b,f,K,h):
    m = int((b-a)/h) + 1
    x = np.zeros(m)
    ff = np.zeros(m)
    K_matrix = np.zeros((m,m))

    # Construct x_i and f(x_i)
    for i in range(m):
        x[i] = a + i*h
        ff[i] =  f(x[i])

    # Construct coeffs matrix
    for i in range(m):
        for j in range(m):
            K_matrix[i,j] = K(x[i],x[j])


    K_matrix[:,1:m-1] *= 2
    K_matrix = np.eye(m) - h * K_matrix

    return K_matrix, ff, x

def K_fun(x,t):
    return np.exp(np.abs(x-t))

def f(x):
    return x**2

for h in [0.25, 0.1, 0.05]:
    A,b,x = fie(0,1,f,K_fun,h)
    sol = GaussPartialPivoting(A,b)
    plt.plot(x,sol)

plt.xlabel("x_i")
plt.ylabel("u(x_i)")
plt.title("Fredholm integral equation of the second kind example")
plt.grid()
plt.show()


