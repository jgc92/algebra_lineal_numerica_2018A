import numpy as np
import matplotlib.pyplot as mtp

def normalize(v,o):
    if o not in [1,2,np.inf]:
        norm_v = sum(abs(v)**o)**(1/o)
    else:
        norm_v = np.linalg.norm(v,o)
        
    return (v/norm_v)

A = np.matrix('-1,3; 2,-4')

def graphP(p):
    for i in range(100):
        unit_v = normalize(np.random.randint(-100,100, (2,1)), p)
        Av = A * unit_v

        sample = np.squeeze(np.asarray(Av))
        mtp.scatter(unit_v[0], unit_v[1], color='b')
        mtp.scatter(sample[0], sample[1], color='r')


for i,p in enumerate([1,1.5,2,2.5,np.inf]):
    mtp.subplot(3,2,i+1)
    graphP(p)
    mtp.title('Grafica para p= ' + str(p))


mtp.show()


    
