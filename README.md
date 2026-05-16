# Fuzzy Cognitive Map Simulation 

This project implements a Fuzzy Cognitive Map to find a causal link between dopamenurgetic content and the goal focusing ability of the brain. 
- There are 3 pre-defined brain types integrated into the system: Disciplined, Average and Distracted

# To run the project
## Install ALL required dependencies:
- pip install numpy 
- pip install matplotlib 

In the root directory, run python ./main.py
- Note: This will save screenshots of the simulation in the Folder: plot_simulations
- Implementation was completed on Python version 3.13.7 and Windows 11. 

# Codebase Explanation 
The codebase for the system follows a basic layered architecture, with clear separation of concerns through decoupling the logic, math equations, scenarios and simulation code into separate files
- logic.py: runs the simulation for a time t, calls scenarios.py and equations at every step
- scenarios.py: defines the 5 scenarios… which represent added variability to monitor how the system responds 
- equations.py: contains implementation for summation and sigmoid function, completes matrix multiplication through np.dot 
- main.py: starts simulations, visualizes results with the matlibplot 
##All the documentation used in the files is highlighted at the top of the code file with a comment. 
- This separation of concern ensures that the code base is easily extendible for future development, as a new developer can simply can simply create new adjacency matrices or extend scenarios.py with their desired fuzzy logic
