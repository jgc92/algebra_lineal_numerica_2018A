from algorithms import *
import numpy as np

A = np.matrix([[-1,-1,0,1],[-1,1,1,0],[1,1,1,1],[2,0,1,0]])

L,U,P = PLUGauss(A)

print("L = ", L)
print("U = ", U)
print("P = ", P)
