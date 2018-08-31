import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.920,2.080,0.001)
p = (x-2)**9
p_exp = x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512
p_nest = ((((((((x-18)*x+144)*x-672)*x+2016)*x-4032)*x+5376)*x-4608)*x+2304)*x-512

plt.figure(1)

plt.subplot(221)
plt.title('p')
plt.plot(x,p)

plt.subplot(222)
plt.title('p expanded')
plt.plot(x,p_exp)

plt.subplot(223)
plt.title('p nested')
plt.plot(x,p_nest)


plt.show()

