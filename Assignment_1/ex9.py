from ex9_functions import *

n = input("Up to what n would you like to perform the Sieve of Erathostenes?\n")

print("Prime numbers up to " + str(n) + ":\n")
print(sieve(int(n)))
