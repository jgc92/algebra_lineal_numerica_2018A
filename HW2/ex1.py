import numpy as np
import matplotlib.pyplot as plt

def weird_matrix(n):
    M = np.zeros((n,n))

    for i in range(n):
        np.fill_diagonal(M[:,i:], np.arange(n-i,0,-1))
        np.fill_diagonal(M[1:,:], np.arange(n-1,0,-1))
        
    return M

def perturbation(MM):
    M = MM.copy()
    m,n = M.shape
    
    M[0,n-2] += 10**-8
    return M


for n in [5,10,15,20]:

    A = weird_matrix(n)
    Ap = perturbation(A)
    E_1 = np.linalg.eigvals(A)
    E_2 = np.linalg.eigvals(Ap)
    dist = np.linalg.norm(E_1 - E_2, 2)
    k = np.linalg.cond(A)

    print("For n = " + str(n) + ":")
    print("||E_1 - E_2|| = " + str(dist))
    print("k_2(A) = " + str(k))
    print("-----------------------------------------------------------------------------")
    print()


    plt.plot(E_1,E_2)
    
plt.legend([5,10,15,20])
plt.xlabel("E_1")
plt.ylabel("E_2")
plt.show()


