from algorithms import *
import numpy as np

A = np.matrix([[2,1,0,0],[-1,3,3,0],[2,-2,1,4],[-2,2,2,5]])

L,U = LUGauss(A)
LL,UU = LUDoolittle(A)

print("Gauss Elimination")
print("L = ", L)
print("U = ", U)
print("--------------------------------")
print("Doolittle")
print("L = ", LL)
print("U = ", UU)


