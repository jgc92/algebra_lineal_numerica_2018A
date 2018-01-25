from numpy import pi, sin

def S(t,n,T):
    # t is of type list

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

def f(t,T):
    # t is of type list
    res = []
    for i in t:
        if 0 < i and i < T/2:
            res.append(1)
        elif i == T/2:
            res.append(0)
        elif T/2 < i and i < T:
            res.append(-1)

    return res
    
