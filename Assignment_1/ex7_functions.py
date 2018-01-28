def grade_conv(grades: list) -> [str]:
    """ Converts 0-100 numeric scale grades to letter grades.
        Args:
            grades: 0-100 numeric scale grade.

        Returns:
            String representing letter grade.
    """

    result = []

    for g in grades:
        g = float(g)

        if 90 < g and g <= 100:
            result.append("A")
        elif 80 < g and g <= 90:
            result.append("B")
        elif 70 < g and g <= 80:
            result.append("C")
        elif 60 < g and g <= 70:
            result.append("D")
        elif 60 > g:
            result.append("F")
        else:
            result.append("Unknown numeric scale grade")
        
    return result
