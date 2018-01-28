def grade_conv(grade):
    g = int(grade)

    if 90 < g and g <= 100:
        result = "A"
    elif 80 < g and g <= 90:
        result = "B"
    elif 70 < g and g <= 80:
        result = "C"
    elif 60 < g and g <= 70:
        result = "D"
    elif 60 > g:
        result = "F"
    else:
        result = "NaN"

    return result

print(grade_conv(90))
        
