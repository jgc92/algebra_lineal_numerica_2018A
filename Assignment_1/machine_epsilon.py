# Machine epsilon

eps = 1.0
new_eps = eps

while eps != new_eps + 1.0:
    new_eps = new_eps/2
    print(new_eps)


print("eps = " + str(eps))
print("new_eps = " + str(new_eps))


    
