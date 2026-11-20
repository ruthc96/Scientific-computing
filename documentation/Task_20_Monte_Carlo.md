# Task 20: Random Numbers and Monte Carlo Methods

## Objective
To estimate the probability that a network server becomes overloaded when incoming demand is uncertain.

## Input Data
- Server capacity: 1000 units
- Mean demand: 850 units
- Standard deviation: 120 units
- Number of simulations: 100,000
- Random seed: 42

## Mathematical Operation
The program generates random demand values using a normal distribution.

A simulation is considered overloaded when:

Demand > Server Capacity

The overload probability is estimated using:

Overload Probability = Number of Overloaded Simulations / Total Simulations

## Output and Interpretation
The program displays the estimated overload probability and the number of overloaded scenarios.

The graph shows the running estimated probability as the number of simulations increases. The estimate should become more stable as more simulations are performed.

## Changed Input
Server capacity is increased from 1000 to 1100 units. The program calculates the overload probability again using the same random demand values.

The probability should decrease because the server can now handle more incoming demand.

## Real-World Application
Network administrators can use Monte Carlo simulation to estimate server-overload risk and plan sufficient server capacity.

Assumption: Incoming demand follows a normal distribution with a mean of 850 and a standard deviation of 120. The simulation uses a fixed random seed so results can be reproduced.
