# Cartesian to Polar.

from numpy import arctan, cos, sin, sqrt

def cart_polar(x,y):
    # r = sqrt(x^2 + y^2) 
    # theta = arctan(y/x)

    r = sqrt(x**2 + y**2)
    theta = arctan(y/x)

    return [r, theta]

def polar_cart(r, theta):
    # x = r * cos(theta)
    # y = r * sin(theta)

    x = r * cos(theta)
    y = r * sin(theta)

    return [x,y]

choice = input("What conversion would you like to perform?\n \tCartesian to Polar (type 1)\n \tPolar to Cartesian (type 2)\n")
choice = int(choice)


if choice == 1:
    x = input("Type x coordiante:\n")
    y = input("Type y coordinate:\n")
 
    coordinates = cart_polar(float(x), float(y))

    print("r = " + str(coordinates[0]) + "\ntheta = " + str(coordinates[1]))

elif choice == 2:
    r = input("Type value of r:\n")
    theta = input("Type value of theta:\n")

    coordinates = polar_cart(float(r),float(theta))

    print("x = " + str(coordinates[0]) + "\ny= " + str(coordinates[1]))

else:
    print("Unknown choice")

