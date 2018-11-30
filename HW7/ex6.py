import numpy as np

def qrMethod(A,k):
    vals = np.zeros(A.shape[0])
    for i in range(k):
        Q,R = np.linalg.qr(A)
        A = R @ Q

        vals = A.diagonal()

    print('Iterations:' + str(k))
    return A



A = np.array([[2,np.sqrt(2),0],[np.sqrt(2),1,0],[0,0,3]])
print(qrMethod(A,5))
