import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Model z = a + bx + cy

x = np.array([0,1,1,2,2,3,3,4,4])
y = np.array([0,1,2,1,2,1,2,1,2])
z = np.array([15.1, 17.9, 12.7, 25.6, 20.5, 35.1, 29.7, 45.4, 40.2])

A = np.zeros((len(x),3))
A[:,0] = 1
A[:,1] = x
A[:,2] = y

Q,R = np.linalg.qr(A)
sol = np.linalg.solve(R, Q.T@z)

xp = np.linspace(0,4,50)
yp = np.linspace(0,2,50)
fn = sol[0] + sol[1]*xp + sol[2]*yp

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z, '*')
ax.plot(xp,yp,fn)
plt.show()
