import numpy as np
import matplotlib.pyplot as plt

# Exponential form y = axe^(bx)
x = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.5, 1.7, 1.8])
y = np.array([0.75, 1.25, 1.45, 1.25, 0.85, 0.55, 0.35, 0.28, 0.18])

A = np.zeros((len(x),2))
A[:,0] = 1
A[:,1] = x

Q,R = np.linalg.qr(A)
sol = np.linalg.solve(R, Q.T@np.log(y/x))

xp = np.linspace(0.1,1.9,50)
fn = np.exp(sol[0]) * xp * np.exp(sol[1]*xp)

plt.plot(x,y, '*')
plt.plot(xp, fn)
plt.show()
