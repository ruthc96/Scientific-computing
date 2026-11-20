
# TASK 10: ROOT FINDING - BISECTION AND FIXED-POINT METHODS

## Objective
To find the temperature where a heat-balance function equals zero.

## Input Values
The temperature interval is initially 20 to 40 degrees.

## Mathematical Operation
The program solves f(T) = T - 25 - 10e^(-T/20) = 0.

## Implementation
SciPy's root_scalar() applies bisection. Fixed-point iteration repeatedly evaluates T = 25 + 10e^(-T/20).

## Output Interpretation
Both methods estimate the temperature at which the heat-balance function becomes zero. The graph shows where the curve crosses the horizontal axis.

## Parameter Modification
The starting interval is changed from [20, 40] to [25, 45]. The estimated root should remain approximately the same.

## Real-World Application
Root finding can estimate equilibrium temperatures in heating and cooling systems.

## Conclusion
Bisection and fixed-point iteration are numerical techniques for approximating equation roots.
