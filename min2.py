import numpy as np
import matplotlib.pylab as plt

A = np.matrix([[1,1,1],[1,2,4],[1,3,9],[1,4,8],[1,5,25],[1,6,36],[1,7,49],[1,8,64],[1,9,81]])
b = np.matrix([[1],[1.5],[2],[3],[4],[5],[8],[10],[13]])

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9]])
Y = np.matrix([[1],[1.5],[2],[3],[4],[5],[8],[10],[13]])

Q,R = np.linalg.qr(A)

params = np.linalg.solve(R,np.dot(np.transpose(Q),b))
print(params)

plt.plot(X,Y,'*')
x = np.arange(0.5,7.5)
y = params[0,0] + params[1,0] * x + params[2,0] * x**2
plt.plot(x,y)

plt.show()
