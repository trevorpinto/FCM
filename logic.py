# core logic for computing the change of the state vector over time
# Documentation for numpy: https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np
from equations import sigmoid_function, equation_calculation

def run_simulation(start_matrix, state_vector_start, iterations, scenario):
    current_state = state_vector_start.copy() # ensure no errors since state vector is pass by reference
    result = []
    result.append(current_state.copy())
    for i in range(iterations):
        current_state = scenario(current_state, i) #apply scenario 

        current_state = equation_calculation(current_state, start_matrix, 2.5) #uses 2.5 lambda value for better visualization

        result.append(current_state.copy()) #record results

    return np.array(result)
    
