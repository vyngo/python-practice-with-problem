import matplotlib.pyplot as plt
import numpy as np
from ex1_cost_function import *
from ex2_derivative_function import *
from ex3_update_value import *
import time

def main():
	
    # Run gradient descent
    eps = 1e-6
    l_rate = 1e-3
    x_op = [2, 2]

    while True:
        x_new = update_optimized_var(x_op, l_rate)
        print('current x: ', x_new)
        # Check break point
        if np.sqrt((x_new[0]-x_op[0])**2 + (x_new[1]-x_op[1])**2) < eps:
            break
        # Update value of x_op with x_new
        x_op = x_new

    print('Optimized variable: x_op = ', x_op)
    print('Optimized value: f(x_op)=', function(x_op))	

if __name__ == '__main__':
    main()
