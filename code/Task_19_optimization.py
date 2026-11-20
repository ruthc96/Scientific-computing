import numpy as np
from scipy.optimize import minimize

# Type A and Type B server allocation
# Cost per unit: A = 12, B = 18
# Capacity per unit: A = 100, B = 170
# Required capacity: at least 1000

def cost(z):
    x, y = z
    return 12*x + 18*y

def capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# Changed input: increase required capacity to 1200
def new_capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1200

new_solution = minimize(
    cost,
    x0=[5, 4],
    method="SLSQP",
    bounds=bounds,
    constraints={
        "type": "ineq",
        "fun": new_capacity_constraint
    }
)

print("\nAfter increasing required capacity:")
print("New allocation:", new_solution.x)
print("New minimum cost:", new_solution.fun)

# Compare nearby whole-server combinations
best_integer = None

for a in range(0, 20):
    for b in range(0, 20):
        capacity = 100*a + 170*b
        if capacity >= 1000:
            total_cost = 12*a + 18*b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("\nBest whole-server solution:", best_integer)
