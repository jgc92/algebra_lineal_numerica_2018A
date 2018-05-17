import numpy as np
import matplotlib.pyplot as plt
A = np.zeros((80,80))

for i in range(80):
    for j in range(80):
        if j == i:
            A[i,j] = 2*i
        elif j == i+2 or j == i-2:
            A[i,j] = 0.5*i
        elif j == i+4 or j==i-4:
            A[i,j]= 0.25*i
        else:
            A[i,j]= 0



plt.imshow(A);
plt.colorbar()
plt.show()
        
        

