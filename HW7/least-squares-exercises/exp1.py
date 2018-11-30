import numpy as np
import matplotlib.pyplot as plt

# Exponential form y = ae^(bx)
#x = np.arange(1,10)
#y = np.array([1, 1.5, 2, 3, 4, 5, 8, 10, 13])

x = np.arange(0.4,2.7,0.4)
y = np.array([800, 975, 1500, 1950, 2900, 3600])

A = np.zeros((len(x),2))
A[:,0] = 1
A[:,1] = x

#Q,R = np.linalg.qr(A)
#sol = np.linalg.solve(R, Q.T@np.log(y))

U, sigma, VT = np.linalg.svd(A)

Sigma = np.zeros(A.shape)
Sigma[:len(sigma),:len(sigma)] = np.diag(sigma)

sol = VT.T @ np.linalg.pinv(Sigma) @ U.T @ np.log(y)

xp = np.linspace(0,2.4,50)
fn = np.exp(sol[0]) * np.exp(sol[1]*xp)

plt.plot(x,y, '*')
plt.plot(xp, fn)
plt.show()
