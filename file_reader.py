# Using json file reader to read file data from json file 
# File Reader Code: https://www.geeksforgeeks.org/python/read-json-file-using-python/
# Documentation for numpy: https://numpy.org/doc/stable/user/absolute_beginners.html

import json
import numpy as np
from enum import Enum

#enum to represent brain types
class brain_type(Enum):
    disciplined = "disciplined_brain"
    average = "average_brain"
    distracted = "distracted_brain"


def load_data_from_json(brain_types):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

            get_type_for_sim = brain_types.value
            if get_type_for_sim not in data:
                raise ValueError("missing brain type in json file")
            
            brain_type = data[get_type_for_sim]
            initial_matrix = np.array(brain_type['matrix'])
            initial_state = np.array(brain_type['state_vector_start'])

            return initial_matrix, initial_state

    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} was not found")
