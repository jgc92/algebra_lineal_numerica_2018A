from ex7_functions import *

n_grades = []

for i in range(0,4):
    grade = input("Numeric grade of student " + str(i+1) +":\n")
    n_grades.append(grade)

new_grades = grade_conv(n_grades)

for i in range(0,4):
    print("\nStudent " + str(i+1) + " Numeric Grade: " + n_grades[i] + " = " + new_grades[i] + ".")
