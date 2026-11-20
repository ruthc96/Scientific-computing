
import numpy as np

# Number of Type A and Type B servers
# Type A: 4 CPU units and 8 GB memory
# Type B: 2 CPU units and 12 GB memory

A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

b = np.array([20.0, 72.0])

# Solve the simultaneous equations
solution = np.linalg.solve(A, b)

residual = b - A @ solution

print("Type A servers:", solution[0])
print("Type B servers:", solution[1])
print("Verification:", A @ solution)
print("Residual:", residual)

# Change CPU usage
b_modified = np.array([24.0, 72.0])
modified_solution = np.linalg.solve(A, b_modified)

print("Modified Type A servers:", modified_solution[0])
print("Modified Type B servers:", modified_solution[1])
