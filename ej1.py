from IterativeSolvers import *
import matplotlib.pyplot as plt

def print_table(lines, separate_head=True):
    """Prints a formatted table given a 2 dimensional array"""
    #Count the column width
    widths = []
    for line in lines:
        for i,size in enumerate([len(x) for x in line]):
            while i >= len(widths):
                widths.append(0)
            if size > widths[i]:
                widths[i] = size

    #Generate the format string to pad the columns
    print_string = ""
    for i,width in enumerate(widths):
        print_string += "{" + str(i) + ":" + str(width) + "} | "
    if (len(print_string) == 0):
        return
    print_string = print_string[:-3]

    #Print the actual data
    for i,line in enumerate(lines):
        print(print_string.format(*line))
        if (i == 0 and separate_head):
            print("-"*(sum(widths)+3*(len(widths)-1)))
              
A1 = np.array([[3,-1,0,0,0,0.5],[-1,3,-1,0,0.5,0],[0,-1,3,-1,0,0],[0,0,-1,3,-1,0],[0,0.5,0,-1,3,-1],[0.5,0,0,0,-1,3]])

b1 = np.array([5/2,3/2,1,1,3/2,5/2])

A2= np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b2= np.array([1,2,3,4,5])

sol1 = jacobi(A1,b1,6)
sol2 = GaussSeidel(A1,b1,6)
sol3 = SOR(A1,b1,1.1,6)
print(sol3)

rows = []
rows.append(("Alg", "solutions"))
rows.append(("Jacobi", str(sol1)))
rows.append(("GS", str(sol2)))
rows.append(("SOR", str(sol3)))
#print_table(rows)

ws = []
errs = []
for w in np.arange(1.0,1.25,0.1):
    x,err= SOR(A1,b1,w,6)
    ws.append(x)
    errs.append(err)
    
plt.plot(np.arange(1,1.25,0.1),errs)
#plt.show()


    
