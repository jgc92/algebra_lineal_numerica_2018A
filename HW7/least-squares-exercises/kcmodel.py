import numpy as np
import matplotlib.pyplot as plt

# K and C model

c = np.array([0.5, 0.8, 1.5, 2.5, 4])
k = np.array([1.1, 2.4, 5.3, 7.6, 8.9])

A = np.zeros((len(c),2))
A[:,0] = 1
A[:,1] = 1/(c**2)

#Q,R = np.linalg.qr(A)
#sol = np.linalg.solve(R, Q.T@(1/k))

U, sigma, VT = np.linalg.svd(A)

Sigma = np.zeros(A.shape)
Sigma[:len(sigma),:len(sigma)] = np.diag(sigma)

sol = VT.T @ np.linalg.pinv(Sigma) @ U.T @ (1/k)

xp = np.linspace(0.5,4,50)
fn = ((1/sol[0])*xp**2)/((sol[1]/sol[0]) + xp**2)

plt.plot(c,k, '*')
plt.plot(xp, fn)
plt.show()
