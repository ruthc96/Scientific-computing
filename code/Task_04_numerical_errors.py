
import numpy as np

# Floating-point comparison
calculated = 0.1 + 0.2
expected = 0.3

print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# Absolute and relative error
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("Absolute error:", absolute_error)
print("Relative error:", relative_error)

# Change the approximation
new_approximation = 1.4142
new_error = abs(true_value - new_approximation)

print("New approximation:", new_approximation)
print("New absolute error:", new_error)
