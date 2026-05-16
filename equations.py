# Documentation for numpy: https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np

def sigmoid_function(x_val, lambda_val):
    val = (1 + np.exp(-lambda_val * x_val))
    return 1 / val 

def equation_calculation(state_vector, adjacency_matrix, lambda_val):
    # perform matrix multiplcation between state_vec & adjacency matrix using np.dot product
    sum_val = np.dot(state_vector, adjacency_matrix)
    x_i = sigmoid_function(sum_val, lambda_val)

    return x_i
