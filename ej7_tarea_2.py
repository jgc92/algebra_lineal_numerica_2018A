import numpy as np
from scipy.linalg import hilbert

def my_cond(M,o):
    M_inv = np.linalg.inv(M)
    k = np.linalg.norm(M,o) * np.linalg.norm(M_inv,o)

    return k

print('Para Hilbert n=5 y my_cond')
for i in [1,np.inf]:
    print('Norma p =' + str(i) + '\tk= ' + str(my_cond(hilbert(5),i)))

print('\n\n\n')

print('Para Hilbert n=3,6,9,12 y np.linalg.cond')
for i in [3,6,9,12]:
    print("Norma p = 1" + '\tk= ' +str(np.linalg.cond(hilbert(i),1)))

print('\n')

for i in [3,6,9,12]:
    print("Norma p = inf" + '\tk= ' +str(np.linalg.cond(hilbert(i),np.inf)))
