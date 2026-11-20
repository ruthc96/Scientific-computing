# Task 18: Numerical Solution of ODEs Using SciPy

## Objective
To simulate population growth using a numerical differential equation solver.

## Input Data
- Initial population: 100
- Growth rate: 0.3
- Simulation period: 0 to 10 time units

## Mathematical Operation
The population growth model is:

dP/dt = rP

Where:
- P is the population.
- r is the growth-rate parameter.
- t is time.

The program uses SciPy's solve_ivp function to approximate the solution of the differential equation.

## Output and Interpretation
The program displays the estimated population at the end of the simulation.

The graph shows population increasing over time. A higher growth rate produces faster population growth.

## Changed Input
The growth rate is increased from 0.3 to 0.4. The final estimated population becomes larger because the population grows faster.

## Real-World Application
This method can model population growth, bacterial growth or other systems that change over time.

Assumption: The growth rate remains constant, and the model does not include limiting resources or environmental changes.
