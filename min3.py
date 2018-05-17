import numpy as np
import matplotlib.pylab as plt

A = np.matrix([[1,1],[1,1.25],[1,1.5],[1,75],[1,2]])
b = np.matrix([[5.10],[5.79],[6.53],[7.45],[8.46]])
b2 = np.log(b)

X = np.array([[0],[0.15],[0.31],[0.5],[0.6],[0.75]])
#Y = np.array([[1],[1.004],[1.031],[1.117],[1.223],[1.422]])
Y = b2

Q,R = np.linalg.qr(A)


params = np.linalg.solve(R,np.dot(np.transpose(Q),b2))

plt.plot(X,Y,'*')
x = np.arange(1,2
              ,0.01)
y = params[0,0] + params[1,0] * x

plt.plot(X,y)

plt.show()
