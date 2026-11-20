# Task 19: Numerical Optimization

## Objective
To find the least expensive allocation of two server types while meeting a minimum processing-capacity requirement.

## Input Data
- Type A cost per unit: 12
- Type B cost per unit: 18
- Type A capacity: 100
- Type B capacity: 170
- Required total capacity: 1000

## Mathematical Operation
The objective is to minimize:

Cost = 12x + 18y

Subject to:

100x + 170y >= 1000

And:

x >= 0, y >= 0

The program uses SciPy's minimize function with the SLSQP method to find an allocation satisfying the constraint at minimum cost.

## Output and Interpretation
The program displays the optimized allocation, total capacity and minimum planning cost.

It also checks nearby whole-server combinations because real servers normally cannot be purchased in fractional quantities.

## Changed Input
The required capacity is increased from 1000 to 1200. The optimization is repeated. A higher capacity requirement generally requires more resources and increases the minimum cost.

## Real-World Application
A cloud service provider can use optimization to allocate server resources while controlling operating costs.

Assumption: Costs and processing capacities per unit are constant. The initial optimization permits fractional allocations; the integer comparison considers whole servers.
