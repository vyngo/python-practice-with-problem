import numpy as np
# name: Ngo Duy Khanh Vy
## x is a list [x_1, x_2]
## return gradient vector
def derivative_function(x):
    der = [0, 0]
    # TODO: compute gradient of the following function: (1−x_1)^2+100(x_2−x_1^2)^2
    der[0] = -2 * (1 -x[0]) + 100 * 2 * (x[1] -(x[0] ** 2)) * -2 * x[0]
    der[1] = 2 * 100 * (x[1] - (x[0] ** 2))
    return der
