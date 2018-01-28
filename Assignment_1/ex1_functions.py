def bmi(weight: float, height: float) -> float:
    """Returns a float number that represents the Body Mass Index (BMI) in metric system (kg/m^2).
    
    Args:
        weight: weight in kg.
        height: height in meters.

    Returns:
        Float number representing BMI.
    """
    result = weight / (height ** 2)
    return result
