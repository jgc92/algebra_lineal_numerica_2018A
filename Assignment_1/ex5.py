from ex5_functions import *
import matplotlib.pyplot as plt

trials = [100, 200, 300, 500, 1000]

# List of matrices to work with
matrices_A = []
matrices_B = []

# Creates random matrices.
for i,n in enumerate(trials):
    matrices_A.append(rand_matrix(n,n))
    matrices_B.append(rand_matrix(n,n))

        
my_times = []
native_times = []

for i in range(len(trials)): # Bad but what the heck, who cares
    my_times.append(take_time(matrices_A[i], matrices_B[i], False))
    native_times.append(take_time(matrices_A[i], matrices_B[i], True))

# Scatter plot.
plt.scatter(trials, my_times)
plt.scatter(trials, native_times)
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Time vs Size Matrix Addition")
plt.legend(["m_add", "native"])
plt.show()
    
    
