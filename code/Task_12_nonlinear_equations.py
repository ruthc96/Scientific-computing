
import numpy as np
from scipy.optimize import root

# Circle: x² + y² = 4
# Parabola: y = x² - 1

def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]

# Solve from two initial guesses
for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)

    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)

# Change initial guess
modified = root(equations, [0.5, 1.5])
print("Modified guess solution:", modified.x)
