import matplotlib.pyplot as plt
import numpy as np
from ex1_cost_function import *
#from ex2_derivative_function import *
from ex3_update_value import *
import time
import tensorflow as tf

def main():
	# Run gradient descent
	l_rate = 0.01
	x = tf.Variable(1, dtype = tf.float32)
	cost = x**4 - 5*x**2 + x + 1
	train = tf.train.GradientDescentOptimizer(l_rate).minimize(cost)
	init = tf.global_variables_initializer()
	sess = tf.Session()
	sess.run(init)
	for i in range(100):
		sess.run(train)
		x_op = sess.run(x)

	print('Optimized variable: x_op = ', x_op)
	print('Optimized value: f(x_op)=', sess.run(cost))	

if __name__ == '__main__':
	main()
