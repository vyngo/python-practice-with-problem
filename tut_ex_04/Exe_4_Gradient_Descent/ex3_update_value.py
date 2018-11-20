from ex2_derivative_function import *
# name: Ngo Duy Khanh Vy
## x_old is the list [x_1, x_2]
def update_optimized_var(x_old, l_rate):
    x_new = [0, 0]
    # TODO: Compute new value x_new based on gradient value and learning rate
    grad = derivative_function(x_old)
    x_new[0] = x_old[0] - l_rate * grad[0]
    x_new[1] = x_old[1] - l_rate * grad[1]
    return x_new
