from ex4_functions import *
from numpy import arange
import matplotlib.pyplot as plt

t = arange(1,6,0.3)
T = 6

ft = f(t,T)

for i in [1,3,5,10,30]:
    St = S(t,i,T)
    plt.plot(t,St)

plt.plot(t,ft)
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("Aproximation of f(t) with S(t;n)")
plt.legend(["f(t)", "n=1", "n=3", "n=5", "n=10", "n=30" ])

plt.show()






