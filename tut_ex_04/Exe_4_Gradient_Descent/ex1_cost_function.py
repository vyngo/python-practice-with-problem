import numpy as np
# name: Ngo Duy Khanh Vy
## x is a list [x_1, x_2]
def function(x):
    y = 0
    # TODO: compute cost value of the following function: (1−x_1)^2+100(x_2−x_1^2)^2
    y = (1-x[0])**2 + 100 * (x[1] - (x[0] ** 2)) ** 2

    return y
