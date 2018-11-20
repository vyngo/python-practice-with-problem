import matplotlib.pyplot as plt
import numpy as np
from ex1_cost_function import *
#from ex2_derivative_function import *
from ex3_update_value import *
import time
import tensorflow as tf

def main():
    # Run gradient descent
    l_rate = 1e-3
    x_0 = tf.Variable(2, dtype = tf.float32)
    x_1 = tf.Variable(2, dtype = tf.float32)
    y = (1 - x_0)**2 + 100*(x_1 - x_0**2)**2
    train = tf.train.GradientDescentOptimizer(l_rate).minimize(y)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    
    for i in range(10000):
        sess.run(train)

    print('Optimized variable: x_op = ', sess.run([x_0, x_1]))
    print('Optimized value: f(x_op)=', sess.run(y))	

if __name__ == '__main__':
    main()
