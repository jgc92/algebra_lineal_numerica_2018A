import numpy as np
import matplotlib.pyplot as plt

# Second degree polynomial

x = np.arange(1,10)
y = np.array([1, 1.5, 2, 3, 4, 5, 8, 10, 13])

A = np.zeros((len(x),3))
A[:,0] = 1
A[:,1] = x
A[:,2] = x**2

Q,R = np.linalg.qr(A)
sol = np.linalg.solve(R, Q.T@y)

xp = np.linspace(1,10,50)
fn = sol[0] + sol[1]*xp + sol[2]*xp**2

plt.plot(x,y, '*')
plt.plot(xp, fn)
plt.show()
