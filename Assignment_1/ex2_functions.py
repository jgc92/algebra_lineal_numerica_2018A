from numpy import arctan, cos, sin, sqrt

def cart_polar(x: float, y: float) -> [float, float]:
    """ Takes cartesian coordinates and returns correspondent polar coordinates.

        Args:
            x: x-coordinate.
            y: y-coordinate.

        Returns:
            Polar coordinates [r-coordinate, theta angle (radians)]
    """

    r = sqrt(x**2 + y**2)

    if y == 0:
        theta = 180 if x < 0 else 0
    elif x == 0:
        theta = 90 if y > 0 else 270
    else:
        theta = arctan(y/x)

    return [r, theta]

def polar_cart(r: float, theta: float) -> [float, float]:
    """ Takes polar coordinates and returns correspondent cartesian coordinates.

        Args:
           r: r-coordinate
           y: y in radians
    """

    x = r * cos(theta)
    y = r * sin(theta)

    return [x,y]

