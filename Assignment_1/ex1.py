from ex1_functions import *

weight = input("How much do you weight? (in kg)\n")
height = input("How tall are you? (in meters)\n")

bmi = bmi(float(weight), float(height))

print("Your BMI is = " + "%.3f" % bmi + "kg/m^2")
