import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def get_Wilkinsons_coeffs():
    x = sym.Symbol('x')
    W = 1
    for i in range(1, 21):
        W *= (x-i)
        
    P,d = sym.poly_from_expr(W.expand())
    return  np.array(P.all_coeffs())


a = get_Wilkinsons_coeffs()
a_roots = np.arange(20,0,-1)

for _ in range(101):
    i = np.random.randint(0,21)
    b = a.copy()
    b[i] = a[i] * (1 + 10**(-10)*np.random.normal(0,1))

    roots = np.roots(b)
    plt.plot(a_roots, roots)
    plt.xlabel("Roots without perturbations")
    plt.ylabel("Roots with perturbations")
    plt.grid()

plt.show()
