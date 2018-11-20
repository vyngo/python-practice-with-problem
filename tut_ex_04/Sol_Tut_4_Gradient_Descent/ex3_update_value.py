from ex2_derivative_function import *


def update_optimized_var(x_old, l_rate):
    x_new = 0
	# TODO: Compute new value x_new based on gradient value and learning rate
    grad = derivative_function(x_old)
    x_new = x_old - l_rate*grad 
    
    return x_new
