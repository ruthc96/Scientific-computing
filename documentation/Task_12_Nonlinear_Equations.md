
# TASK 12: POLYNOMIAL AND NONLINEAR EQUATION SOLVING

## Objective
To find intersection points between a circle and a parabola.

## Input Values
Circle: x² + y² = 4.
Parabola: y = x² - 1.

## Mathematical Operation
The equations are solved simultaneously by finding values that make both residuals zero.

## Implementation
SciPy's root() function estimates the unknown x and y values using initial guesses.

## Output Interpretation
The output gives the intersection coordinates. Small residuals indicate that the equations are approximately satisfied.

## Parameter Modification
The initial guess is changed to [0.5, 1.5]. The solver attempts to locate an intersection from this starting point.

## Real-World Application
Nonlinear equation solving is useful in engineering, geometric modelling and chemical equilibrium calculations.

## Conclusion
Numerical solvers help find solutions to equations that cannot easily be solved analytically.
