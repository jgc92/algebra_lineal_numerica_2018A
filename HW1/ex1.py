from ex1_functions import *

choice = input("What conversion would you like to perform?\n \tCartesian to Polar (type 1)\n \tPolar to Cartesian (type 2)\n")
choice = int(choice)

# Polar conversion.
if choice == 1:
    x = input("Type x coordiante:\n")
    y = input("Type y coordinate:\n")
 
    coordinates = cart_polar(float(x), float(y))

    print("\nr = " + "%.3f" % coordinates[0] + "\ntheta = " + "%.3f" % coordinates[1])

# Cartesian convertion.
elif choice == 2:
    r = input("Type value of r:\n")
    theta = input("Type value of theta:\n")

    coordinates = polar_cart(float(r),float(theta))

    print("\nx = " + "%.3f" % coordinates[0] + "\ny= " + "%.3f" % coordinates[1])

else:
    print("Unknown choice")

