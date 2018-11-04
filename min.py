import numpy as np
import matplotlib.pylab as plt

A = np.matrix([[1,0],[1,0.15],[1,0.31],[1,0.5],[1,0.6],[1,0.75]])
b = np.matrix([[1],[1.004],[1.031],[1.117],[1.223],[1.422]])

X = np.array([[0],[0.15],[0.31],[0.5],[0.6],[0.75]])
Y = np.array([[1],[1.004],[1.031],[1.117],[1.223],[1.422]])

Q,R = np.linalg.qr(A)

params = np.linalg.solve(R,np.dot(np.transpose(Q),b))

plt.plot(X,Y,'*')
x = np.arange(0,1,0.01)
y = params[0,0] + params[1,0] * x
print(y)
plt.plot(x,y)

#plt.show()

