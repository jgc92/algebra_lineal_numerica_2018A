from numpy import pi, sin

def S(t: list, n: int, T: float) -> list:
    """ Fourier Series Aproximation for f(t).

        Args:
            t: list of values of t.
            T: constant T.

        Result:
            List with aproximations of f(t)
    """

    result = []
    for m in t:
        my_sum = 0
        for i in range(n+1):
            x = 2*(i+1) - 1
            y = pi * m

            my_sum = my_sum + (1/x) * sin((2*x*y)/T)

        res = (4/pi) * my_sum
        result.append(res)

    return result

def f(t: list ,T: float) -> list:
    """ Piecewise function:
            | 1, 0 < t < T/2
      f(x)= | 0, t = T/2
            | -1, T/2 < t < T

        Args:
            t: list of values of t.
            n: times to iterate
            T: constant T

        Result:
            List with values of f(t).
    """

    res = []
    for i in t:
        if 0 < i and i < T/2:
            res.append(1)
        elif i == T/2:
            res.append(0)
        elif T/2 < i and i < T:
            res.append(-1)

    return res
    
