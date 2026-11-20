import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Generate random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

# Identify overloaded scenarios
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices]
)
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo Estimate of Server-Overload Risk")
plt.grid(True)
plt.savefig("task20_monte_carlo.png")
plt.show()

# Changed input: increase server capacity
new_capacity = 1100.0
new_overloaded = demand > new_capacity
new_probability = new_overloaded.mean()

print("\nAfter increasing server capacity:")
print(f"New estimated overload probability: {new_probability:.4%}")
