# Machine epsilon

eps = 1.0
new_eps = eps

while eps != new_eps + 1.0:
    new_eps = new_eps/2

print("Machine Epsilon = " + str(new_eps))


    
