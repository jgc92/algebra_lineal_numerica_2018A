from algorithms import *
import numpy as np


A = np.matrix([[2.12,-2.12, 51.3, 100],[0.333, -0.333, -12.2, 19.7],[6.19, 8.20, -1, -2.01],[-5.73, 6.12, 1, -1]])
b = np.matrix([np.pi, np.sqrt(2), 0, -1])

s1 = GaussSimple(A,b)
s2 = GaussPartialPivoting(A,b)

print("Solution with partial pivoting:")
print(s2)
